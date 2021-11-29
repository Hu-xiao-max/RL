import gym
env = gym.make("CartPole-v0")#MountainCar-v0、CartPole-v0
#http://gym.openai.com/docs/
observation = env.reset()
for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  observation, reward, done, info = env.step(action)

  if done:
    observation = env.reset()
env.close()