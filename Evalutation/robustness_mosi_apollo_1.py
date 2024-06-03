import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data
epsilon_values = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
robustness_values = np.array([2.1231, 2.1551, 2.43309, 2.1551, 2.2935, 2.2321, 2.6809, 2.6595])

# Interpolation
x_smooth = np.linspace(epsilon_values.min(), epsilon_values.max(), 300)
spl = make_interp_spline(epsilon_values, robustness_values, k=3)
robustness_smooth = spl(x_smooth)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, robustness_smooth, color='b', marker='o')

# Labels and title
plt.xlabel('ϵ values', fontsize=14)
plt.ylabel('Robustness', fontsize=14)
# plt.title('Smoothed Robustness Curve', fontsize=16)

# Save the figure as PDF file
plt.savefig('/Users/honghuixu/Desktop/smoothed_robustness_mosi_apollo_1.pdf', format='pdf')

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()