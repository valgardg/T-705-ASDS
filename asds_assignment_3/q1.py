import numpy as np
from scipy.stats import norm, chi2

observed_frequencies = np.array([12, 32, 30, 20, 6])
total_employees = 100
mean_height = 170
std_dev_height = 10
significance_level = 0.05

ranges = [(150, 159), (160, 169), (170, 179), (180, 189), (190, 199)]

expected_frequencies = []
for lower, upper in ranges:
    prob = norm.cdf(upper, mean_height, std_dev_height) - norm.cdf(lower, mean_height, std_dev_height)
    expected_frequencies.append(prob * total_employees)

expected_frequencies = np.array(expected_frequencies)

chi_square_statistic = np.sum((observed_frequencies - expected_frequencies)**2 / expected_frequencies)

degrees_of_freedom = len(ranges) - 1

critical_value = chi2.ppf(1 - significance_level, degrees_of_freedom)

if chi_square_statistic > critical_value:
    result = "Reject the null hypothesis."
else:
    result = "Fail to reject the null hypothesis."

print("Observed Frequencies:", observed_frequencies)
print("Expected Frequencies:", expected_frequencies)
print("Chi-Square Statistic:", chi_square_statistic)
print("Critical Value:", critical_value)
print("Conclusion:", result)
