import numpy as np
import matplotlib.pyplot as plt

# Provided values
data = {
    "MISA": [0.4154, 0.7972, 0.8092, 0.7857, 0.7847],
    "Self-MM": [0.4244, 0.8079, 0.8066, 0.783, 0.7834],
    "MMIM": [0.433, 0.8208, 0.8173, 0.799, 0.7984],
    "APOLLO II (ϵ = 0.5)": [0.38921, 0.79573, 0.79646, 0.77842, 0.77843],
    "APOLLO II (ϵ = 1.0)": [0.38192, 0.81402, 0.81515, 0.80758, 0.80811],
    "APOLLO II (ϵ = 1.5)": [0.37755, 0.8064, 0.80679, 0.78862, 0.7883],
    "APOLLO II (ϵ = 2.0)": [0.41399, 0.81707, 0.81797, 0.80758, 0.80795],
    "APOLLO II (ϵ = 2.5)": [0.40087, 0.78963, 0.79001, 0.77551, 0.7752],
    "APOLLO II (ϵ = 3.0)": [0.37026, 0.79725, 0.79844, 0.79008, 0.79065],
    "APOLLO II (ϵ = 3.5)": [0.40524, 0.7942, 0.79539, 0.78425, 0.78481],
    "APOLLO II (ϵ = 4.0)": [0.38775, 0.79725, 0.79844, 0.78279, 0.78334]
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
# plt.title('Performance Comparison on MOSI Dataset (Baselines v.s. Apollo II with Various ϵ)', fontsize=18, fontweight='bold')
plt.xticks(x + bar_width * (len(all_labels) / 2 - 0.5), metrics, fontsize=12, rotation=0)
plt.yticks(fontsize=12)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the figure as an EPS file
plt.savefig('/Users/honghuixu/Desktop/performance_comparison_mosi_apollo_2.pdf', format='pdf')

plt.show()