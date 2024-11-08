import scipy.stats as stats

observed = [[45, 5], [30, 20]]

chi2_stat, p_value, dof, expected = stats.chi2_contingency(observed)

alpha = 0.05

print(f"Chi-square Statistic: {chi2_stat:.2f}")
print(f"P-value: {p_value:.4f}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)