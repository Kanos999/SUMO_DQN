import os
import sys

import gymnasium as gym
from stable_baselines3.dqn.dqn import DQN


if "SUMO_HOME" in os.environ:
    tools = os.path.join(os.environ["SUMO_HOME"], "tools")
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")
import traci

from sumo_rl import SumoEnvironment


if __name__ == "__main__":
  env = SumoEnvironment(
    net_file="intersection/environment.net.xml",
    route_file="intersection/episode_routes.rou.xml",
    out_csv_name="outputs/intersection/dqn",
    single_agent=True,
    use_gui=True,
    num_seconds=5400,
    yellow_time=4,
    min_green=5,
    max_green=60,
  )

  model = DQN(
    env=env,
    policy="MlpPolicy",
    verbose=1,
    train_freq=16,
    gradient_steps=8,
    gamma=0.99,
    exploration_fraction=0.2,
    exploration_final_eps=0.07,
    target_update_interval=5000,
    learning_starts=1000,
    buffer_size=25000,
    batch_size=128,
    learning_rate=4e-3,
    policy_kwargs=dict(net_arch=[256, 256]),
    double_q=False
  )
  model.learn(total_timesteps=100000)