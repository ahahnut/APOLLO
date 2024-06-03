import numpy as np
import matplotlib.pyplot as plt

# Provided values
data = {
    "MISA": [0.5249, 0.844, 0.842, 0.8173, 0.8193],
    "Self-MM": [0.5159, 0.8122, 0.825, 0.7944, 0.7995],
    "MMIM": [0.5237, 0.8223, 0.8351, 0.79, 0.7966],
    "APOLLO II (ϵ = 0.5)": [0.50623, 0.84651, 0.84646, 0.80747, 0.81297],
    "APOLLO II (ϵ = 1.0)": [0.52385, 0.83934, 0.84068, 0.7978, 0.80524],
    "APOLLO II (ϵ = 1.5)": [0.52191, 0.83742, 0.83796, 0.8021, 0.80826],
    "APOLLO II (ϵ = 2.0)": [0.52148, 0.841, 0.83969, 0.81671, 0.81987],
    "APOLLO II (ϵ = 2.5)": [0.51568, 0.84596, 0.84433, 0.82402, 0.82645],
    "APOLLO II (ϵ = 3.0)": [0.52148, 0.85064, 0.85027, 0.81779, 0.82226],
    "APOLLO II (ϵ = 3.5)": [0.51697, 0.84182, 0.84252, 0.80296, 0.8094],
    "APOLLO II (ϵ = 4.0)": [0.51933, 0.84761, 0.84694, 0.82079, 0.82456]
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
# plt.title('Performance Comparison on MOSEI Dataset (Baselines v.s. Apollo II with Various ϵ)', fontsize=18, fontweight='bold')
plt.xticks(x + bar_width * (len(all_labels) / 2 - 0.5), metrics, fontsize=12, rotation=0)
plt.yticks(fontsize=12)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the figure as an EPS file
plt.savefig('/Users/honghuixu/Desktop/performance_comparison_mosei_apollo_2.pdf', format='pdf')

plt.show()