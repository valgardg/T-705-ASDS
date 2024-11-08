from scipy.stats import f

s_X = 0.6  # Server A 
s_Y = 1.2  # Server B

df2 = 29  # Server A
df1 = 19  # Server B

var_X = s_X ** 2 # Server A 
var_Y = s_Y ** 2 # Server B

F_ratio = var_Y / var_X

# critical F values
F_lower = f.ppf(0.025, df2, df1)
F_upper = f.ppf(0.975, df2, df1)

CI_lower = F_ratio * F_lower
CI_upper = F_ratio * F_upper

print(f'CI_lower: {CI_lower}\nCI_upper: {CI_upper}')