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

    def update(self, observations):
        # convert the observation array into a matrix with 1 column and ninputs rows
        observation.resize(ninputs,1)
        # compute the netinput of the first layer of neurons
        Z1 = np.dot(self.W1, observation) + self.b1
        # compute the activation of the first layer of neurons with the tanh function
        A1 = np.tanh(self.Z1)
        # compute the netinput of the second layer of neurons
        Z2 = np.dot(self.W2, A1) + self.b2
        # compute the activation of the second layer of neurons with the tanh function
        A2 = np.tanh(self.Z2)
        # if the action is discrete
        #  select the action that corresponds to the most activated unit
        if (isinstance(env.action_space, gym.spaces.box.Box)):
            action = A2
        else:
            action = np.argmax(A2)

        return action
    
    def evaluate(self, nepisodes):
        cumreward = 0
        for e in range(nepisodes):
            observation = env.reset()
             
            while not done:
                action = network.update(observation)
                step = env.step(action)
                observations, reward, done, info = step
                cumreward += reward
                
        return cumreward/nepisodes

    def getnparameters(self):
        self.paramvec =
        return nparameters

    def setparameters(self, genotype):

popsize = 10 
generange = 0.1
mutrange = 0.02
nepisodes = 3
ngenerations = 100
env = gym.make("CartPole-v0")

print(env.observation_space.shape)  # (4,)
print(env.action_space.n)   # 2 = nmotorn


network = Network(env, 5)
nparameters = network.getnparameters()
population = the size should be popsize*nparameters
fitness = []
for g in range(ngenerations):
    for i in range(popsize):
        network.setparameters(population[i])
        fit = network.evaluate(nepisodes)
        fitness.append((fit,i))
    fitness.sort(key=lambda y: y[0])
    for i in range(popsize/2):
        population[3] = population[7] + random vector with range mutrange


fitness = network.evaluate(3)