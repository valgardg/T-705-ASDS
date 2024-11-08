import numpy as np
import matplotlib.pyplot as plt

heights = [72, 75, 78, 80, 82, 85, 68, 75, 79, 77, 80, 76, 81, 74, 72, 88, 91, 83, 85, 79, 
           82, 70, 77, 75, 74, 78, 81, 83, 79, 82, 84, 85, 76, 74, 80, 79, 88, 92, 73, 82, 
           86, 80, 78, 77, 74, 84, 83, 81, 87, 85]

n_bootstrap = 10000

bootstrap_medians = []

for _ in range(n_bootstrap):
    bootstrap_sample = np.random.choice(heights, size=len(heights), replace=True)
    bootstrap_medians.append(np.median(bootstrap_sample))

lower_bound = 75
upper_bound = 80

count_in_range = sum(lower_bound <= median <= upper_bound for median in bootstrap_medians)

probability = count_in_range / n_bootstrap
print(f"Estimated Probability that the median is between {lower_bound} and {upper_bound}: {probability}")