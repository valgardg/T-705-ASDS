import numpy as np
import scipy.stats as stats

spam_counts = np.array([
    12, 6, 4, 0, 13, 5, 1, 3, 10, 1, 29, 12, 4, 4, 22,
    2, 2, 27, 7, 27, 9, 34, 10, 10, 2, 28, 7, 0, 9, 4,
    32, 4, 5, 9, 1, 13, 10, 20, 5, 5, 0, 6, 9, 20, 28,
    22, 10, 8, 11, 15, 1, 14, 0, 9, 9, 1, 9, 0, 7, 13
])

lambda_estimate = np.mean(spam_counts)

observed_counts = np.bincount(spam_counts) 
observed_counts = observed_counts[observed_counts > 0]
num_days = len(spam_counts)

max_count = len(observed_counts) - 1
poisson_probs = [stats.poisson.pmf(k, lambda_estimate) for k in range(max_count + 1)]

expected_counts = np.array(poisson_probs) * num_days

observed_counts_combined = []
expected_counts_combined = []
for obs, exp in zip(observed_counts, expected_counts):
    if exp < 5:
        if not observed_counts_combined:
            observed_counts_combined.append(obs)
            expected_counts_combined.append(exp)
        else:
            observed_counts_combined[-1] += obs
            expected_counts_combined[-1] += exp
    else:
        observed_counts_combined.append(obs)
        expected_counts_combined.append(exp)

observed_counts_combined = np.array(observed_counts_combined)
expected_counts_combined = np.array(expected_counts_combined)

chi_square_stat = np.sum((observed_counts_combined - expected_counts_combined) ** 2 / expected_counts_combined)
degrees_of_freedom = len(observed_counts_combined) - 1 - 1 
critical_value = stats.chi2.ppf(0.99, degrees_of_freedom)

print("Lambda (Mean):", lambda_estimate)
print("Observed Counts (after combining):", observed_counts_combined)
print("Expected Counts (after combining):", expected_counts_combined)
print("Chi-Square Statistic:", chi_square_stat)
print("Critical Value at 0.01 significance level:", critical_value)

if chi_square_stat < critical_value:
    print("Conclusion: Fail to reject the null hypothesis. Data follows a Poisson distribution.")
else:
    print("Conclusion: Reject the null hypothesis. Data does not follow a Poisson distribution.")
