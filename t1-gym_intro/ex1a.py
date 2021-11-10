import time
import gym

env = gym.make('Pendulum-v0')
env.reset()

print("\n************ env Starting ************")

print("                      Min    Max")
print("endpoint y position   {0}   {1} \nAngle                 {2}   {3} \nAngularVelocity       {4}   {5}".format(
str(round(env.observation_space.low[0],2)), str(round(env.observation_space.high[0],2)), 
str(round(env.observation_space.low[1],2)), str(round(env.observation_space.high[1],2)), 
str(round(env.observation_space.low[2],2)), str(round(env.observation_space.high[2],2))    ))

time.sleep(2)

cumreward = 0
for _ in range(1000):
    env.render()
    action = env.action_space.sample()
    step = env.step(action) # take a random action
    observations, reward, done, info = step
    yposition, angle, angvel = round(observations[0],3), round(observations[1],3), round(observations[2],3)
    cumreward += reward

    reward = round(reward,3)
    action = round(action[0],3)
    cumreward = round(cumreward,3)
    print ("action  y-position  anlge     angVel  reward   cumreward    done    info\n {0}{1}{2}{3}{4}{5}".format(str(action).ljust(10), 
    str(yposition).ljust(10), str(angle).ljust(10), str(angvel).ljust(8), str(reward).ljust(10), str(cumreward).ljust(10), str(done).ljust(10), info))

    time.sleep(0.2)

    if done:
        # env.reset()
        print(info)
        time.sleep(3)
        break

env.close()

