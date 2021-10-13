import gym 
from gym import error, spaces, utils
import time
from stable_baselines import DQN
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.common.evaluation import evaluate_policy
import self_balance

environment_name = 'self_balance-v0'
env = gym.make(environment_name)

env = DummyVecEnv([lambda: env])
model = DQN('MlpPolicy', env, verbose = 2)


model.learn(total_timesteps=83000)

evaluate_policy(model, env, n_eval_episodes=10, render=True)
env.close()

model.save("DQN_model")

print("############################################################################")
print("practice complete")
print("############################################################################")
