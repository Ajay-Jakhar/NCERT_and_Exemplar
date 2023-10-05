# Probability of getting 6 on the first die
p_first_die_6 = 1/2
# Probability of getting 1 on the first die
p_first_die_1 = 1/10

# Probability of getting 1 on the second die
p_second_die_1 = 2/5

# Probability of not getting 1 on the second die
p_second_die_not_1 = 1 - p_second_die_1

# Calculate probabilities for different outcomes
# Number of ones seen can be 0, 1, or 2

# Probability of getting 0 ones
p_zero_ones = (1 - p_first_die_1) * p_second_die_not_1

# Probability of getting 1 one
p_one_ones = p_first_die_1 * p_second_die_not_1 + p_second_die_1 * (1 - p_first_die_1)

# Probability of getting 2 ones
p_two_ones = p_first_die_1 * p_second_die_1

# Print the probability distribution
print("Probability of 0 ones:", p_zero_ones)
print("Probability of 1 one:", p_one_ones)
print("Probability of 2 ones:", p_two_ones)

