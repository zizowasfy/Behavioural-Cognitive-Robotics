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
        
        self.neuralNet()

    #ToDo give the number of network layers as a input parameter to neuralNet() *update not necessary; the architecture should be added manually 
    def neuralNet(self, params=0):         # This funciton creates the architecture of the Neural Network 

        pvariance = 0.1     # variance of initial parameters
        ppvariance = 0.02   # variance of perturbations
        nhiddens = 5        # number of internal neurons

        if np.any(params) == True:  # params not zeros = not the initial iteration
            sub1 = nhiddens*self.nsensoryn
            sub2 = sub1 + self.nmotorn*nhiddens
            sub3 = sub2 + nhiddens
            sub4 = sub3 + self.nmotorn
            # print(sub4) # for debugging should be 37 in this example

            splitparams = np.split(params,[sub1, sub2, sub3, sub4])
            self.W1 = splitparams[0].reshape(nhiddens,self.nsensoryn)
            self.W2 = splitparams[1].reshape(self.nmotorn,nhiddens)
            self.b1 = splitparams[2].reshape(nhiddens,1)
            self.b2 = splitparams[3].reshape(self.nmotorn,1)

        else:       # params are zeros = initial iteration
            self.W1 = np.random.randn(nhiddens,self.nsensoryn) * pvariance   # first connection layer
            self.W2 = np.random.randn(self.nmotorn, nhiddens) * pvariance    # second connection layer
            self.b1 = np.zeros(shape=(nhiddens, 1))                          # bias internal neurons
            self.b2 = np.zeros(shape=(self.nmotorn, 1))  
            params = np.expand_dims(np.concatenate((self.W1.ravel() , self.W2.ravel(), self.b1.ravel(), self.b2.ravel())), axis=0)
            self.nparameters = params.shape[1]   # number of parameter in the whold neural network = (37,)
            
        return params

    def update(self, observation):      # Apply the feed-forward to output the trained action of the environment

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
        else:
            action = np.argmax(A2)

        return action
    
    def evaluate(self, nepisodes):      # Evaluate each genotype (individual) through nepisodes and calculate the cumulative reward
        cumreward = 0
        for e in range(nepisodes):
            observation = env.reset()
            done = False
            while not done:
                action = network.update(observation)
                step = env.step(action)
                observation, reward, done, info = step
                cumreward += reward
                
        return cumreward/nepisodes

    def getnparameters(self):
        return self.nparameters

    # def setparameters(self, genotype):

popsize = 10
generange = 0.1
mutrange = 0.02
nepisodes = 3
ngenerations = 10
avgthreshold = 20   #20
maxthreshold = 200  #200
env = gym.make("CartPole-v0")

# print(env.observation_space.shape)  # (4,)
# print(env.action_space.n)   # 2 = nmotorn


network = Network(env, 5)
nparameters = network.getnparameters()

# population = the size should be popsize*nparameters
rank = []
popparams = np.zeros((popsize, nparameters))

g, avgpopfitness, maxpopfitness = 0, 0, 0
try:    
    # for g in range(ngenerations):
    while maxpopfitness < maxthreshold:         # Loop until the fitness of generation reaches a pre-defined threshold
        for i in range(popsize):                # Evalualte each genotype of every population and calculate its fitness
            params = network.neuralNet(popparams[i][:])
            fit = network.evaluate(nepisodes)
            rank.append((fit,i))
            popparams[i][:] = params
            # popfitness += fit
        rank.sort(key=lambda x: x[0])           # Rank the genotypes of the current population according to their fitness
        
        for j in range(int(popsize/2)):         # Replace the first half (low fitness) of the population with the other half (high fitness)  
            ind_sorted = rank[j][1] # index of the first 5 individuals from the rank sorted list
            popparams[ind_sorted][:] = popparams[j+int(popsize/2)][:] + np.random.randn(1,nparameters)*mutrange

        print("\n*** NEW GENERATION IS REBORN ***")
        print ("Generation = ",g)
        g += 1
        maxpopfitness = rank[-1][0]
        print("Population Max fitness = ", maxpopfitness)
        avgpopfitness = (rank[-1][0] + rank[0][1]) / popsize
        print("Population Average fitness = ", avgpopfitness)
        # if maxpopfitness > threshold:
        #     break
except KeyboardInterrupt:
    print('interrupted!')

