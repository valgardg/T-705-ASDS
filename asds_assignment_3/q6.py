import numpy as np
from scipy import stats

incomes = np.array([125.5, 130.3, 133.0, 102.6, 198.0, 232.5, 106.8, 114.5, 122.0, 100.0, 118.8, 108.6, 312.7, 125.5])

median_1987 = 124.4

differences = incomes - median_1987

positive_signs = np.sum(differences > 0)
negative_signs = np.sum(differences < 0)
zero_signs = np.sum(differences == 0)

n = len(differences) - zero_signs
test_statistic_sign_test = min(positive_signs, negative_signs)

p_value_sign_test = stats.binom.cdf(test_statistic_sign_test, n, 0.5)

non_zero_differences = differences[differences != 0] # we dont want zero differences so we remove them
statistic_wilcoxon, p_value_wilcoxon = stats.wilcoxon(non_zero_differences)

print(f"Sign Test:")
print(f" - Test Statistic: {test_statistic_sign_test}")
print(f" - p-value: {p_value_sign_test:.4f}\n")

print(f"Wilcoxon Signed Rank Test:")
print(f" - Test Statistic: {statistic_wilcoxon}")
print(f" - p-value: {p_value_wilcoxon:.4f}")
