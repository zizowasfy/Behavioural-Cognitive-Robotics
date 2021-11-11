import time
import gym
import numpy as np

class Network:
    def __init__(self, env, nhiddens):

        self.nhiddens = nhiddens

        ninputs = env.observation_space.shape[0]
        if (isinstance(env.action_space, gym.spaces.box.Box)):
            noutputs = env.action_space.shape[0]
        else:
            noutputs = env.action_space.n

        self.nsensoryn = ninputs
        self.nmotorn = noutputs

        pvariance = 0.1     # variance of initial parameters
        ppvariance = 0.02   # variance of perturbations
        nhiddens = 5        # number of internal neurons
        self.W1 = np.random.randn(nhiddens,ninputs) * pvariance      # first connection layer
        self.W2 = np.random.randn(noutputs, nhiddens) * pvariance    # second connection layer
        self.b1 = np.zeros(shape=(nhiddens, 1))                      # bias internal neurons
        self.b2 = np.zeros(shape=(noutputs, 1))   

    def update(self, observation):
        # convert the observation array into a matrix with 1 column and ninputs rows
        observation.resize(self.nsensoryn,1)
        # compute the netinput of the first layer of neurons
        Z1 = np.dot(self.W1, observation) + self.b1
        # compute the activation of the first layer of neurons with the tanh function
        A1 = np.tanh(Z1)
        # compute the netinput of the second layer of neurons
        Z2 = np.dot(self.W2, A1) + self.b2
        # compute the activation of the second layer of neurons with the tanh function
        A2 = np.tanh(Z2)
        # if the action is discrete
        #  select the action that corresponds to the most activated unit
        if (isinstance(env.action_space, gym.spaces.box.Box)):
            action = A2
            # print("Continous action")

        else:
            action = np.argmax(A2)
            # print("Discrete action")

        return action
    
    def evaluate(self, nepisodes):
        cumreward = 0
        for e in range(nepisodes):
            observation = env.reset()
            done = False
            while not done:
                action = network.update(observation)
                step = env.step(action)
                observations, reward, done, info = step
                cumreward += reward
                print("action= ",action)
                print("step= ",step)
                print("cumreward= ",cumreward)
        return cumreward/nepisodes

env = gym.make("CartPole-v1")

print(env.observation_space.shape)  # (4,)
print(env.action_space.n)   # 2 = 2 motor actions; either +1(right) or 0(left)

network = Network(env, 5)
fitness = network.evaluate(3)
print("fitness= ",fitness)