import numpy as np
import matplotlib.pyplot as plt

# Baseline values
baseline_values = {
    "MISA": [0.4154, 0.7972, 0.8092, 0.7857, 0.7847],
    "Self-MM": [0.4244, 0.8079, 0.8066, 0.783, 0.7834],
    "MMIM": [0.433, 0.8208, 0.8173, 0.799, 0.7984]
}

# Model values
model_values = {
    "APOLLO I (ϵ = 0.5)": [0.3775, 0.81097, 0.81036, 0.79737, 0.7962],
    "APOLLO (ϵ = 1.0)": [0.3862, 0.81707, 0.8174, 0.8032, 0.80297],
    "APOLLO I (ϵ = 1.5)": [0.4037, 0.81097, 0.81115, 0.79154, 0.79096],
    "APOLLO I (ϵ = 2.0)": [0.41107, 0.81554, 0.81624, 0.80466, 0.80483],
    "APOLLO I (ϵ = 2.5)": [0.40233, 0.8064, 0.80533, 0.77988, 0.7775],
    "APOLLO I (ϵ = 3.0)": [0.4169, 0.80487, 0.80533, 0.79154, 0.7918],
    "APOLLO I (ϵ = 3.5)": [0.4067, 0.81402, 0.80574, 0.793, 0.79272],
    "APOLLO I (ϵ = 4.0)": [0.41836, 0.81402, 0.81485, 0.80466, 0.81485]
}

# Metrics labels
metrics = ['Acc-7', 'Acc-2 (Pos/Neg)', 'F1 (Pos/Neg)', 'Acc-2 (Non-neg/Neg)', 'F1 (Non-neg/Neg)']

# Combine all values for plotting
all_labels = list(baseline_values.keys()) + list(model_values.keys())
all_values = list(baseline_values.values()) + list(model_values.values())

# Tetradic color palette
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
# plt.title('Performance Comparison on MOSI Dataset (Baselines v.s. Apollo I with Various ϵ)', fontsize=18, fontweight='bold')
plt.xticks(x + bar_width * (len(all_labels) / 2 - 0.5), metrics, fontsize=12, rotation=0)
plt.yticks(fontsize=12)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the figure as an EPS file
plt.savefig('/Users/honghuixu/Desktop/performance_comparison_mosi_apollo_1.pdf', format='pdf')

plt.show()