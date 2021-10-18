import gym 
from gym import error, spaces, utils
import time
from stable_baselines import DQN
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.common.evaluation import evaluate_policy
import self_balance

environment_name = 'self_balance-v0'
env = gym.make(environment_name)
print("############################################################################")
print("This is learnt bot")
print("############################################################################")
model = DQN.load("DQN_model", env=env)

obs = env.reset()
while True:
    action, _states = model.predict(obs)
    #print("hello")
    obs, rewards, done, info = env.step(action)
    if done:
    	env.reset()
    env.render('human')
    
env.close()
