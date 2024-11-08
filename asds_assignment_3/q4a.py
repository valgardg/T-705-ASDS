import numpy as np
from scipy import stats

heights = np.array([
    72, 75, 78, 80, 82, 85, 68, 75, 79, 77, 80, 76, 81, 74, 72, 88, 91, 83, 85, 79,
    82, 70, 77, 75, 74, 78, 81, 83, 79, 82, 84, 85, 76, 74, 80, 79, 88, 92, 73, 82,
    86, 80, 78, 77, 74, 84, 83, 81, 87, 85
])

mu_0 = 74.3

sample_mean = np.mean(heights)
sample_std = np.std(heights, ddof=1)
n = len(heights)

t_stat = (sample_mean - mu_0) / (sample_std / np.sqrt(n))

alpha = 0.05
df = n - 1
t_critical = stats.t.ppf(1 - alpha, df)

p_value = 1 - stats.t.cdf(t_stat, df)

print("Sample Mean:", sample_mean)
print("Sample Standard Deviation:", sample_std)
print("t-Statistic:", t_stat)
print("Critical t-Value:", t_critical)
print("p-Value:", p_value)

if t_stat > t_critical:
    print("Reject the null hypothesis: There is enough evidence to support the claim that the plants are growing taller.")
else:
    print("Fail to reject the null hypothesis: There is not enough evidence to support the claim that the plants are growing taller.")
