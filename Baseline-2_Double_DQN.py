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


from stable_baselines3 import DQN

# Initialize the environment (SumoEnvironment)
env = SumoEnvironment(
    net_file=r"intersection\environment.net.xml",
    route_file=r"intersection\episode_routes.rou.xml",
    out_csv_name=r"outputs\intersection_DoubleDQN\dqn",
    single_agent=True,
    use_gui=True,
    num_seconds=5400,
    yellow_time=4,
    min_green=5,
    max_green=60,
)

# Define policy_kwargs to enable Double DQN
policy_kwargs = dict(
    net_arch=[128, 128],  
)

# Initialize the DQN model with Double DQN enabled via policy_kwargs
model = DQN(
    "MlpPolicy",  # Using a Multi-layer Perceptron policy
    env,
    learning_rate=1e-3,
    learning_starts=0,
    buffer_size=50000,
    train_freq=1,
    target_update_interval=500,
    exploration_fraction=0.05,
    exploration_final_eps=0.01,
    verbose=1,
    policy_kwargs=policy_kwargs,  # Pass policy_kwargs for additional configuration
)

model.learn(total_timesteps=100000)

