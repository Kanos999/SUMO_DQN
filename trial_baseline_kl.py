import os
import sys
import gymnasium as gym
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory

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

    nb_actions = env.action_space.n

    # Build a simple neural network model
    model = Sequential()
    model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
    model.add(Dense(256, activation='relu'))
    model.add(Dense(256, activation='relu'))
    model.add(Dense(nb_actions, activation='linear'))

    # Configure and compile the agent
    memory = SequentialMemory(limit=25000, window_length=1)
    policy = EpsGreedyQPolicy()
    dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=1000,
                   target_model_update=5000, policy=policy, train_interval=16, delta_clip=1.0)
    dqn.compile(Adam(lr=4e-3), metrics=['mae'])

    # Train the agent
    dqn.fit(env, nb_steps=100000, visualize=False, verbose=1)