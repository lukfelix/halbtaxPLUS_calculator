import numpy as np
import matplotlib.pyplot as plt
import config


def sim_year(expected=False):
    nums = {}
    for key in config.routes:
        nums[key]=0.

    if expected:
        for key in config.weekly_expected:
            nums[key] += config.n_weeks*config.weekly_expected[key][2]

        for key in config.yearly_expected:
            nums[key] += config.yearly_expected[key][2]
    else:
        for key in config.weekly_expected:
            nums[key] += np.sum(
                np.random.randint(
                config.weekly_expected[key][0], 
                config.weekly_expected[key][1]+1, # +1 is needed for convention of randint
                size=config.n_weeks))
                
        for key in config.yearly_expected:
            nums[key] += np.sum(
                np.random.randint(
                config.yearly_expected[key][0], 
                config.yearly_expected[key][1]+1, 
                size=1))

    return nums

def calc_cost(nums):
    cost = 0.
    for key in nums:
        cost += config.routes[key]*nums[key]
    
    return cost

def halbtax_adjustment(cost):
    tier=0
    # figure out which halbtax option to buy
    # if above critical value, need to go up a tier
    for val in config.halbtax_plus_crit:
        if cost < val:
            break
        else: tier += 1
    
    if cost < config.halbtax_plus_options[tier]:
        cost = config.halbtax_plus_prices[tier]
    else: 
        cost -= (config.halbtax_plus_options[tier]
                 -config.halbtax_plus_prices[tier])
        

    cost += config.halbtax_price
    
    return cost

def get_distribution(num=100):

    costs = []
    for i in range(num):
        ns = sim_year()
        costs.append(halbtax_adjustment(calc_cost(ns)))
    
    costs= np.array(costs)

    return costs.reshape(-1)

def expected_cost():
    nums = sim_year(expected=True)
    cost = halbtax_adjustment(calc_cost(nums))
    return cost

def plot(expected, costs):

    mean, std, med = np.mean(costs), np.std(costs), np.median(costs)
    print(mean, std, med)

    fig = plt.figure(figsize=(10, 7))
    plt.hist(costs, alpha=0.5, color='darkorange')
    plt.axvline(mean, linestyle='--', label='Mean')
    plt.axvline(med, linestyle='-', label='Median')
    plt.axvline(expected, linestyle='--', label='Your expected Case', color='red')
    plt.axvspan(mean-std, mean+std, alpha=0.2, label='1-sigma deviation')
    plt.axvline(3495., linestyle='-', label='GA25', color='black')
    plt.axvline(3995., linestyle='-', label='GA', color='grey')
    
    plt.xlabel('CHF')
    plt.legend()
    plt.savefig('results/costs.pdf')
    # plt.show()

    
    return

####################################################
# This runs the script
####################################################
expected = expected_cost()
costs = get_distribution(num=1000)
plot(expected, costs)