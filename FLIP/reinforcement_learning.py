# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:33:53 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make("MountainCar-v0")
state = env.reset()
print(env.observation_space.high)
LEARNING_RATE = 0.1
DISCOUNT = 0.95 #how important do we find future actions how much we value future reward over current reward and its a vlaue between zero and 1
EPISODES = 25000
SHOW_EVERY=2000
DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
print(DISCRETE_OS_SIZE)
#new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
# per episode reward tracking system is probably good  solution rather than simply picking discount and otiher vlaues

epsilon = 0.5 # this is the randomness
START_EPISOLON_DECAYING = 1
END_EPSILON_DECAYING = EPISODES//2
epsilon_decay_value =epsilon/(END_EPSILON_DECAYING-START_EPISOLON_DECAYING)

# how big is that number are those chunks
discrete_os_win_size = (env.observation_space.high-env.observation_space.low )/DISCRETE_OS_SIZE
q_table = np.random.uniform(low=-2,high=0,size=(DISCRETE_OS_SIZE+ [env.action_space.n] ))


ep_rewards=[]
aggr_ep_rewards = {"ep": [], "avg": [], "min": [], "max": []}
# what lookign for or to optimize for will change depenidng on the task you're trying to acheive
# need to convert continmous states to discrete states
def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low)/ discrete_os_win_size
    return tuple(discrete_state.astype(np.int))
#print(discrete_state)
#print(np.argmax(q_table[discrete_state]))
# highest value for all observations possible
#print(env.observation_space.low)
#lowest value for all observations possible
#print(env.action_space.n)
# usually know actions in advance
# want q table of size that is managementable
# discrete observation space
# might want 50 and 20 but going to use 20 and 20 for now

# these are the bucket sizes and this is granular enough
# now its only 20 by 20
# so 400 combinations
# backpropgate that reward
# generated table of random starting q value
#print(q_table.shape)
#print(discrete_os_win_size)
# -1 on every frame so if you could find a quicker way to acheive objective that would be superior.
# reward is a negative 1 until you reach the flag then it gets a zero reward which is better than negative 1 and then we backproproage that chain of events.
for episode in range(EPISODES):
    discrete_state = get_discrete_state(env.reset()[0])
    #print(discrete_state)
   # print(q_table[discrete_state])
   # print(q_table)

    done = False

    episode_reward = 0
    if episode % SHOW_EVERY ==0: # if can divide by 2000 and the remainder is zero
        #print(episode)
        render=True
    
    while not done:
        
        if np.random.random()>epsilon:            # creates random float between zero and 1 if greater than epsilon value actions in regulator way otherwise action is random
            action = np.argmax(q_table[discrete_state])
            #print(action)
        else:
            action= np.random.randint(0,env.action_space.n) #.n means number of actions
            # once finds one way to the fly it will keeep triyng that way to get to the flag so that is why we need to explore the space.

            
        new_state, reward, done, _, dog = env.step(action)
        episode_reward+= reward
        print(done)
        new_discrete_state= get_discrete_state(new_state)
        
        
        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
            current_q= q_table[discrete_state + (action,)]
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            q_table[discrete_state + (action,)]= new_q
        elif new_state[0] >= env.goal_position:
            
            print(f"we made it on episode {episode}")
            #q_table[discrete_state + (action,)] = reward
            q_table[discrete_state + (action,)]= 0
        discrete_state=new_discrete_state
        


        if END_EPSILON_DECAYING >= episode >= START_EPISOLON_DECAYING:
            epsilon -= epsilon_decay_value
        ep_rewards.append(episode_reward)
        if not episode % SHOW_EVERY:
            average_reward= sum(ep_rewards[-SHOW_EVERY:])/len(ep_rewards[-SHOW_EVERY:])
            aggr_ep_rewards['ep'].append(episode)
            aggr_ep_rewards['avg'].append(average_reward)
            aggr_ep_rewards['min'].append(min(ep_rewards[-SHOW_EVERY:]))
            aggr_ep_rewards['max'].append(max(ep_rewards[-SHOW_EVERY:]))
            #print(f" episdoe {episode}, avg: {average_reward} max {max(ep_rewards[-SHOW_EVERY:])}")

            
            
        
        
            
        #print(reward, new_state)
env.close()
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['avg'], label = "avg")
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['min'], label = "min")
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['max'], label = "max")
plt.legend(loc=4)
plt.show()


