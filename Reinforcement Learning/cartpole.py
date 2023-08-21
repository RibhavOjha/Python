import gym as gym
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers.legacy import Adam
import numpy as np
import random
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory


env = gym.make("CartPole-v1")
states = env.observation_space.shape[0]
actions = env.action_space.n    
# del model
model = Sequential()
model.add(Flatten(input_shape=(1,states)))
model.add(Dense(512, activation='relu'))
model.add(Dense(1024, activation='relu'))
model.add(Dense(actions, activation='linear'))
# model.add(Flatten())
model.summary()
agent = DQNAgent(model=model, 
                memory=SequentialMemory(limit = 500000, window_length = 1), 
                policy=BoltzmannQPolicy(),
                nb_actions=actions,
                nb_steps_warmup=10, 
                target_model_update=1e-2)   

agent.compile(Adam(lr=1e-3), metrics=['mae'])
agent.fit(env, nb_steps=10000, visualize=False, verbose=1)

results = agent.test(env, nb_episodes=10, visualize=True)
print(np.mean(results.history['episode_reward']))
env.close()



