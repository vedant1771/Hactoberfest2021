'''hello everyone! I am Pratyush and below is the code of our 2-wheeled robot environment. 

To check different cases, you could change the values of Torque(by changing the values in array whose one value(randomly for bot learning) is assigned to self.tar_vel in bot_practice_action function) and checkout whether it improves stability of bot. 

You could also change control from torque control to velocity control if you want ''' 

import os
import time
import math
import numpy as np
import gym
import random
from gym import spaces
from gym.utils import seeding
import pybullet as p
import pybullet_data

class self_balance(gym.Env):
    def __init__(self):
        self._observation = []
        self.action_space = spaces.Discrete(13)
        self.observation_space = spaces.Box(low = np.array([-math.pi, -math.pi, -5]),high = np.array([math.pi, math.pi, 5]))
        self.physicsClient = p.connect(p.GUI)
        self.right_action=[]
        self._seed()
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.i=0
        self.vt = 0
        
    
    def bot_practice_action(self, action):
        
        #random_velocity= np.random.uniform(9.9, 20.08 , 8)
        #ml=random.choice([1, -1])
        #self.tar_vel= ml*random_velocity[action]
                
        #print(self._observation[0])
        
        #if(self._observation[0]>0):
        	#self.tar_vel= random_velocity[action]
        #if(self._observation[0]<0):
        	#self.tar_vel= -random_velocity[action]
        	
        self.tar_vel=[-16.3,-16,-15,-14 ,-13, -12, -11, 11 ,12 ,13 ,14, 15 ,16.3][action]        
        right_joint=1
        left_joint=0
        Max_velocity=0
        p.setJointMotorControl2(bodyUniqueId=self.botId,jointIndex=left_joint,controlMode=p.TORQUE_CONTROL,force=self.tar_vel)
        p.setJointMotorControl2(bodyUniqueId=self.botId,jointIndex=right_joint,controlMode=p.TORQUE_CONTROL,force=self.tar_vel)
        

    def tell_observation(self):
        cubePos, cubeOrn = p.getBasePositionAndOrientation(self.botId)
        cubeEuler = p.getEulerFromQuaternion(cubeOrn)
        linear, angular = p.getBaseVelocity(self.botId)
        
        #print(cubeEuler)
        return [cubeEuler[0], angular[0], self.tar_vel]

    def tell_reward(self):
        unused_variable, cubeOrn = p.getBasePositionAndOrientation(self.botId)
        cubeEuler = p.getEulerFromQuaternion(cubeOrn)
        return (math.pi/2-abs(cubeEuler[0]))
    
    def check_done(self):
        cubePos, _ = p.getBasePositionAndOrientation(self.botId)
        if cubePos[2] < 0.05:
            self.i+=1
            if self.i >1000:
                done = True
            else:
                done = False
        else: 
            done = False
            self.i = 0  
        return done or self.practice_time_interval >= 5200
	
    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        print(seed)
        return [seed]
    
    def _step(self, action):
        self.bot_practice_action(action)
        p.stepSimulation()
        #time.sleep(1/240)
        self._observation = self.tell_observation()
        reward = self.tell_reward()
        done = self.check_done()
        if(done==1):
        	self.set()

        self.practice_time_interval += 1

        return np.array(self._observation), reward, done, {}

    def _reset(self):
        self.tar_vel = 0
        self.vd = 0
        self.practice_time_interval = 0

        p.resetSimulation()
        p.setGravity(0, 0, -9.8)
        #p.setTimeStep(0)
        planeId = p.loadURDF("plane.urdf")
        cubeStartPos = [0, 0, 0.01]
        cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 0])

        path = os.path.abspath(os.path.dirname(__file__))
        self.botId = p.loadURDF(os.path.join(path, "balancebot_simple.urdf"), cubeStartPos, cubeStartOrientation)

        self._observation = self.tell_observation()
        return np.array(self._observation)


    def _render(self, mode='human', close=False):
    	pass


    def set(self):
        self.tar_vel = 0
        self.vd = 0
        self.practice_time_interval = 0

        
        cubeStartPos = [0, 0, 0.01]
        cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
        
        p.resetBasePositionAndOrientation(bodyUniqueId=self.botId,posObj=cubeStartPos,ornObj=cubeStartOrientation)

        
        
    
