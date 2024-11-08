import numpy as np
from scipy.stats import f

s_X = 0.6  # Standard deviation for Server A
s_Y = 1.2  # Standard deviation for Server B
n = 30     # Sample size for Server A
m = 20     # Sample size for Server B

# F-statistic
F_statistic = (s_Y ** 2) / (s_X ** 2)

df2 = n - 1  # for Server A
df1 = m - 1  # for Server B

# two-tailed p-value
p_value = 2 * min(f.cdf(F_statistic, df1, df2), 1 - f.cdf(F_statistic, df1, df2))

F_statistic, p_value
print(f'F_statistic: {F_statistic}\np_value: {p_value}')