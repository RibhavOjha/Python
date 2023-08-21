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
# Random moves
episodes = 10
for i in range(1, episodes + 1):
    state = env.reset()
    done = False
    score = 0
    while not done:
        #action
        action = random.choice([0,1])
        n_state ,reward, done, info = env.step(action)
        env.render()
        score += reward
        
    print('Episode:{} Score:{}'.format(i, score))
env.close()