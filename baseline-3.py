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

  model = PPO(
    policy="MlpPolicy",
    env=env,
    verbose=1,
    gamma=0.99,
    n_steps=2048,
    ent_coef=0.0,
    learning_rate=4e-3,
    vf_coef=0.5,
    max_grad_norm=0.5,
    gae_lambda=0.95,
    batch_size=64,
    n_epochs=10,
    clip_range=0.2,
    policy_kwargs=dict(net_arch=[256, 256])
  )
  model.learn(total_timesteps=100000)