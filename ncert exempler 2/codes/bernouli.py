from scipy.stats import bernoulli

# Probability of success (p) - selecting an envelope with no cash prize
p = 0.69

# Create a Bernoulli random variable with the specified probability
rv = bernoulli(p)

# Probability of X = 1 (success)
probability_X_equals_1 = rv.pmf(1)

print("Probability of selecting an envelope with no cash prize (X = 1):", probability_X_equals_1)

