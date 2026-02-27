import gym
from web_agent_site.envs.web_agent_site_env import WebAgentSiteEnv

# Initialize the environment
# Note: Ensure the server_url matches what your run_dev.sh showed (usually 5000)
env = WebAgentSiteEnv(observation_mode='text',render=True, server_url="http://127.0.0.1:5000")

# Reset the environment to get the initial State and Goal
obs, info = env.reset()

print("-" * 30)
print(f"GOAL/INSTRUCTION: {env.observation}")
print(f"INITIAL STATE (Observation): {obs[:1000]}...") # Printing first 500 chars
print(f"AVAILABLE ACTIONS: {env.get_available_actions()}")
print("-" * 30)

action = 'search[red color women faux fur lined winter warm jacket coat]'
obs, reward, done, info = env.step(action)
print('TEST TEST TEST')
print(f"OBSERVATION: {obs}")
print(f"REWARD: {reward}")
print(f"DONE: {done}")
print(f"INFO: {info}")
print(f"AVAILABLE ACTIONS: {env.get_available_actions()}")
print("-" * 30)