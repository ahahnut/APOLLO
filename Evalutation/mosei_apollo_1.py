import numpy as np
import matplotlib.pyplot as plt

# Provided values
data = {
    "MISA": [0.5249, 0.844, 0.842, 0.8173, 0.8193],
    "Self-MM": [0.5159, 0.8122, 0.825, 0.7944, 0.7995],
    "MMIM": [0.5237, 0.8223, 0.8351, 0.79, 0.7966],
    "APOLLO I (ϵ = 0.5)": [0.51052, 0.83549, 0.83593, 0.7948, 0.80139],
    "APOLLO I (ϵ = 1.0)": [0.51504, 0.84045, 0.84095, 0.79673, 0.80343],
    "APOLLO I (ϵ = 1.5)": [0.51568, 0.83962, 0.8394, 0.80446, 0.80974],
    "APOLLO I (ϵ = 2.0)": [0.51869, 0.84816, 0.84825, 0.80962, 0.81515],
    "APOLLO I (ϵ = 2.5)": [0.51353, 0.84706, 0.8452, 0.82799, 0.82979],
    "APOLLO I (ϵ = 3.0)": [0.51998, 0.8443, 0.8441, 0.80855, 0.8137],
    "APOLLO I (ϵ = 3.5)": [0.52599, 0.83135, 0.83273, 0.77352, 0.78259],
    "APOLLO I (ϵ = 4.0)": [0.51675, 0.83852, 0.83941, 0.80038, 0.8071]
}

# Metrics labels
metrics = ['Acc-7', 'Acc-2 (Pos/Neg)', 'F1 (Pos/Neg)', 'Acc-2 (Non-neg/Neg)', 'F1 (Non-neg/Neg)']

# Combine all values for plotting
all_labels = list(data.keys())
all_values = list(data.values())

# Pastel color palette
pastel_colors = [
    "#aec7e8", "#ffbb78", "#98df8a", "#ff9896",
    "#c5b0d5", "#c49c94", "#f7b6d2", "#c7c7c7",
    "#dbdb8d", "#9edae5", "#ffcc99"
]

# Plotting
bar_width = 0.08
x = np.arange(len(metrics))

plt.figure(figsize=(20, 10))

for i, (label, values) in enumerate(zip(all_labels, all_values)):
    plt.bar(x + i * bar_width, values, width=bar_width, color=pastel_colors[i % len(pastel_colors)], 
            edgecolor='black', label=label)

plt.xlabel('Metrics', fontsize=14)
plt.ylabel('Values', fontsize=14)
# plt.title('Performance Comparison on MOSEI Dataset (Baselines v.s. Apollo I with Various ϵ)', fontsize=18, fontweight='bold')
plt.xticks(x + bar_width * (len(all_labels) / 2 - 0.5), metrics, fontsize=12, rotation=0)
plt.yticks(fontsize=12)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the figure as an EPS file
plt.savefig('/Users/honghuixu/Desktop/performance_comparison_mosei_apollo_1.pdf', format='pdf')

plt.show()