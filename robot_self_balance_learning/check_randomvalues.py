import gym 
from gym import error, spaces, utils
import time
from stable_baselines import DQN
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.common.evaluation import evaluate_policy
import self_balance

environment_name = 'self_balance-v0'
env = gym.make(environment_name)

episodes = 10
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0 
    
    while not done:
        
        env.render('human')
        action = env.action_space.sample()
        #print("action=",action)
        n_state, reward, done, info = env.step(action)
        score+=reward
        #print("reward, done=", reward , done)
    print('Episode:{} Score:{}'.format(episode, score))
env.close()


