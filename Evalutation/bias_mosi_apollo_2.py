import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data
epsilon_values = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
robustness_values = np.array([0.86362, 0.85236, 0.85965, 0.85371, 0.83865, 0.83105, 0.83227, 0.82371])

# Interpolation
x_smooth = np.linspace(epsilon_values.min(), epsilon_values.max(), 300)
spl = make_interp_spline(epsilon_values, robustness_values, k=3)
robustness_smooth = spl(x_smooth)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, robustness_smooth, color='r', marker='^')

# Labels and title
plt.xlabel('ϵ values', fontsize=14)
plt.ylabel('Bias', fontsize=14)
# plt.title('Smoothed Robustness Curve', fontsize=16)

# Save the figure as EPS file
plt.savefig('/Users/honghuixu/Desktop/smoothed_bias_mosi_apollo_2.pdf', format='pdf')

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()