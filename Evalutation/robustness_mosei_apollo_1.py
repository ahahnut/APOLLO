import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data
epsilon_values = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
robustness_values = np.array([1.8331, 1.79533, 1.81983, 1.71673, 1.7346, 1.76056, 1.89214, 1.9550])

# Interpolation
x_smooth = np.linspace(epsilon_values.min(), epsilon_values.max(), 300)
spl = make_interp_spline(epsilon_values, robustness_values, k=3)
robustness_smooth = spl(x_smooth)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, robustness_smooth,color='g', marker='s')

# Labels and title
plt.xlabel('ϵ values', fontsize=14)
plt.ylabel('Robustness', fontsize=14)
# plt.title('Smoothed Robustness Curve', fontsize=16)

# Save the figure as EPS file
plt.savefig('/Users/honghuixu/Desktop/smoothed_robustness_mosei_apollo_1.pdf', format='pdf')

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()