import time
import gym

env = gym.make('MountainCarContinuous-v0')
env.reset()

print("\n************ env Starting ************")
print("\nIn this example, Observations of Car's Position and Velocity are in y-axis")
print("           Min    Max")
print("Position   {0}    {1} \nVelocity   {2}   {3}".format(str(round(env.observation_space.low[0],2)), str(round(env.observation_space.high[0],2)), 
str(round(env.observation_space.low[1],2)), str(round(env.observation_space.high[1],2))))
time.sleep(5)
# action = -1.0
for _ in range(1000):
    env.render()
    # action = [action + 0.01]
    action = env.action_space.sample()
    step = env.step(action) # take a random action
    observations, reward, done, info = step

    position, velocity = round(observations[0],3), round(observations[1],3)
    reward = round(reward,3)
    action = round(action[0],3)
    print ("action  Car Position  Car Velocity  reward    done    info\n {0}{1}{2}{3}{4}{5}".format(str(action).ljust(10), 
    str(position).ljust(15), str(velocity).ljust(10), str(reward).ljust(10), str(done).ljust(10), info))

    time.sleep(0.1)

    if done:
        # env.reset()
        print(info)
        time.sleep(3)
        break

env.close()

