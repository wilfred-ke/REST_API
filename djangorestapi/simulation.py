import numpy as np
"""
# Define the function to integrate
def f(x):
    return 1 / (1 + np.sqrt(x))

# Define integration limits
a = 1  # Lower limit
b = 4  # Upper limit

# Number of random points to sample
N = 15

# Generate random points in the integration domain
x_values = np.random.uniform(a, b, N)

# Evaluate the function at the sampled points
f_values = f(x_values)

# Calculate the integral estimate
integral_estimate = np.mean(f_values) * (b - a)

print("Monte Carlo integral estimate:", integral_estimate)
print('\n', x_values)
for i in f_values:
    print('\n', i)

def f(x, y):
    return 1 / (x + y)

# integral limits
x_min, x_max = 1, 2
y_min, y_max = 1, 2

# number of random points to be sampled
N = 15

# generate random points in the integration domain
x_values = np.random.uniform(x_min, x_max, N)
y_values = np.random.uniform(y_min, y_max, N)

# evaluating the function at sampled points
f_values = f(x_values, y_values)

# calculating integral estimates
integral_estimate = np.mean(f_values)*((x_max - x_min) * (y_max - y_min))

print('\n', x_values)
print('\n', y_values)
print('\n', f_values)
print("\n Monte Carlo Integral estimate: ", integral_estimate)

print('number 2')
import random


import random

def simulate_coin_tosses():
    # Initialize the number of tosses and heads count
    num_tosses = 0
    heads_count = 0

    # Continue tossing until two heads are obtained
    while heads_count < 2:
        # Increment the number of tosses
        num_tosses += 1

        # Simulate the toss of two coins
        coin1 = random.choice(['H', 'T'])
        coin2 = random.choice(['H', 'T'])

        # Check if both coins are heads
        if coin1 == 'H' and coin2 == 'H':
            heads_count += 2
        elif coin1 == 'H' or coin2 == 'H':
            heads_count += 1

    # Return the number of tosses required
    return num_tosses

def estimate_average_tosses(num_simulations):
    # Initialize the total number of tosses
    total_tosses = 0

    # Perform the simulations
    for _ in range(num_simulations):
        total_tosses += simulate_coin_tosses()

    # Calculate the average number of tosses
    average_tosses = total_tosses / num_simulations

    # Return the average number of tosses
    return average_tosses

# Set the number of simulations
num_simulations = 10000

# Estimate the average number of tosses required
average_tosses = estimate_average_tosses(num_simulations)

# Print the estimated average number of tosses
print(f"The estimated average number of tosses required to get two heads for the first time is: {average_tosses}")
"""
import random

# Bearing life distribution
bearing_life = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
bearing_prob = [0.10, 0.14, 0.24, 0.14, 0.12, 0.10, 0.06, 0.05, 0.03, 0.02]

# Delay time distribution
delay_time = [4, 6, 8]
delay_prob = [0.3, 0.6, 0.1]

# Constants
bearing_change_time = {1: 20, 2: 30, 3: 40}
downtime_cost_per_minute = 10
repairman_cost_per_hour = 25
bearing_cost = 30


# Function to simulate bearing failure and replacement
def simulate_policy(policy):
    total_cost = 0

    for _ in range(15):
        # Simulate bearing failure
        bearing_life_hours = random.choices(bearing_life, weights=bearing_prob)[0]
        downtime_cost = bearing_life_hours * downtime_cost_per_minute

        # Simulate delay time
        delay_minutes = random.choices(delay_time, weights=delay_prob)[0]

        # Calculate bearing change time
        bearings_to_replace = 3 if policy == 'alternative' else 1
        bearing_change_time_minutes = bearing_change_time[bearings_to_replace]

        # Calculate repairman cost
        repairman_cost = (delay_minutes + bearing_change_time_minutes) * repairman_cost_per_hour / 60

        # Calculate total cost
        total_cost += downtime_cost + repairman_cost + bearings_to_replace * bearing_cost

    return total_cost


# Simulate existing policy (replace one bearing at a time)
existing_policy_cost = simulate_policy('existing')

# Simulate alternative policy (replace all three bearings at once)
alternative_policy_cost = simulate_policy('alternative')

print("Total cost for existing policy:", existing_policy_cost)
print("Total cost for alternative policy:", alternative_policy_cost)

if existing_policy_cost < alternative_policy_cost:
    print("The existing policy is cheaper.")
elif existing_policy_cost > alternative_policy_cost:
    print("The alternative policy is cheaper.")
else:
    print("Both policies have the same total cost.")
