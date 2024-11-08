import numpy as np
import matplotlib.pyplot as plt

heights = [72, 75, 78, 80, 82, 85, 68, 75, 79, 77, 80, 76, 81, 74, 72, 88, 91, 83, 85, 79, 
           82, 70, 77, 75, 74, 78, 81, 83, 79, 82, 84, 85, 76, 74, 80, 79, 88, 92, 73, 82, 
           86, 80, 78, 77, 74, 84, 83, 81, 87, 85]

n_bootstrap = 10000
bootstrap_medians = []

for i in range(n_bootstrap):
    bootstrap_sample = np.random.choice(heights, size=len(heights), replace=True)
    bootstrap_medians.append(np.median(bootstrap_sample))


sorted_bootstrap_medians = np.sort(bootstrap_medians)

lower_percentile = 2.5
upper_percentile = 97.5

lower_bound_ci = np.percentile(sorted_bootstrap_medians, lower_percentile)
upper_bound_ci = np.percentile(sorted_bootstrap_medians, upper_percentile)

print(f"95% Bootstrap Confidence Interval for the Median: ({lower_bound_ci}, {upper_bound_ci})")
