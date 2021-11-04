## Exercsies' analysis


### ex1b_1 [MountainCar-v0]
<p align="center" >
<img src="https://user-images.githubusercontent.com/70958856/140198668-a21ede27-4a0d-4f18-8a10-d491e7b34adb.png" width="300" height="200">
</p>

The car in this environment is trying to climb up the hill to reach the flag. The environment provides some attritubes:
- action: 0 accelerate to the left ; 1 don't accelerate ; 2 accelerate to the right
- observation: Car position in the y-axis ; Car velocity in the y-axis
- reward: if the car reaches more than half the distance (0.5), it will give a reward of 0 ; -1 otherwise.
- done: check whether the environment reaches any of the termination conditions, reachTimeLimit ; exceed a certain position ; ...   
- info: provide some logging information.

In this demo, no training was done; instead, uniform random ranged actions are given to the car. However, at every env.reset() command, a new episode begins with random initial actions, thus the initial position of the car changes from one episode to another.

<p align="center" >
<img src="https://user-images.githubusercontent.com/70958856/140199026-59ecfb46-7ffd-4ec3-a83c-50074dd3b2a2.png" width="500" height="80">
</p>


### ex1b_2 [MountainCarContinuous-v0]

In this environment, both the action and the reward are continous not discrete as the previous example. 
- action: describes the power coefficient. Continous over the range [-1,1]. 
- reward: ranges from [0,100] where 100 when the car reaches the flag; decreases proportionally with the amount of energy consumed.

<p align="center" >
<img src="https://user-images.githubusercontent.com/70958856/140207215-da896bab-1e99-4ef3-b901-54c44b829c7c.png" width="500" height="80">
</p>

## References
1- https://gym.openai.com/envs/#classic_control

2- https://github.com/openai/gym/blob/master/gym/envs/classic_control/continuous_mountain_car.py
