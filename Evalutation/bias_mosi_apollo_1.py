import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data
epsilon_values = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
robustness_values = np.array([0.8322, 0.82884, 0.82166, 0.81981, 0.81929, 0.81986, 0.81798, 0.81669])

# Interpolation
x_smooth = np.linspace(epsilon_values.min(), epsilon_values.max(), 300)
spl = make_interp_spline(epsilon_values, robustness_values, k=3)
robustness_smooth = spl(x_smooth)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, robustness_smooth, color='b', marker='o')

# Labels and title
plt.xlabel('ϵ values', fontsize=14)
plt.ylabel('Bias', fontsize=14)
# plt.title('Smoothed Robustness Curve', fontsize=16)

# Save the figure as EPS file
plt.savefig('/Users/honghuixu/Desktop/smoothed_bias_mosi_apollo_1.pdf', format='pdf')

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()