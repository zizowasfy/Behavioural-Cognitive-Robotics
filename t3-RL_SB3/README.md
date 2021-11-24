### In this task, an agent is trained to acheieve a certain goal. The training is carried out using stable-baseline3 (SB3) library; which is a Reinforcement Learning implementation supporting many policy algorithms (e.g: PPO, HER, A2C, ...) 

1. Clone the stable-baseline3-zoo library in which it has pre-trained agents that can be retrained, plot results, and visulaize.
```
git clone https://github.com/DLR-RM/rl-baselines3-zoo
```
2. Using docker, pull the already built image (cpu or gpu)
```
docker pull stablebaselines/rl-baselines3-zoo-cpu
```
3. Train the agent (MountainCarContinuous) using PPO algorithm
```
./scripts/run_docker_cpu.sh python train.py --algo ppo --env MountainCarContinuous-v0 
```
The trained policy, model config, and evaluations are saved in ``` /logs/ppo/MountainCarContinuous-v0_1 ``` 

4. Evaluale the agent and obsereve the mean episode and mean reward
```
./scripts/run_docker_cpu.sh python enjoy.py --algo ppo --env MountainCarContinuous-v0 
```
5. Record a video for the agent while training with the last and best 
```
./scripts/run_docker_cpu.sh python -m utils.record_training --algo ppo --env MountainCarContinuous-v0 -f logs --deterministic
```


### References
- https://github.com/DLR-RM/rl-baselines3-zoo
- https://bacrobotics.com/Chapter13.html
