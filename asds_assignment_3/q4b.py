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

plt.figure(figsize=(10, 6))
plt.hist(bootstrap_medians, bins=30, edgecolor='black', color='skyblue')
plt.title('Bootstrap Distribution of the Median Plant Height')
plt.xlabel('Median Height (cm)')
plt.ylabel('Frequency')
plt.grid(True)

plt.savefig('bootstrap_distribution.png') # had to save file due to issue with plot being interactive and system not supporting viewing it
