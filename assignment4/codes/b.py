import random

# Number of trials
num_trials = 100000

# Initialize counters for event A and event B
count_A = 0
count_B = 0
count_A_and_B = 0

# Simulate the trials
for _ in range(num_trials):
    # Simulate the coin toss (event A)
    coin_toss = random.randint(0, 1)  # 0 for tails, 1 for heads

    # Simulate the die roll (event B)
    die_roll = random.randint(1, 6)

    if coin_toss == 1:
        count_A += 1
    if die_roll == 3:
        count_B += 1
    if coin_toss == 1 and die_roll == 3:
        count_A_and_B += 1

# Calculate probabilities using random variables
prob_A = count_A / num_trials
prob_B = count_B / num_trials
prob_A_and_B = count_A_and_B / num_trials
# Check for independence by comparing with the product of probabilities
independence_check = abs(prob_A_and_B - (prob_A * prob_B)) < 0.001  # Use a small threshold for floating-point comparison

if independence_check:
    print("Events A and B are independent.")
else:
    print("Events A and B are not independent.")
