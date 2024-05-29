import matplotlib.pyplot as plt

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(7, 7))

# Adjust spacing
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

# Fill each subplot with a square
for i in range(7):
    for j in range(7):
        if (i == 0 and 2 <= j <= 4) or (i == 1 and j == 1) or (i == 2 and j == 0) or (i == 3 and j == 0) or (i == 4 and j == 1) or (i == 5 and 2 <= j <= 4) or (i == 6 and 3 <= j <= 4):
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color='blue'))
        else:
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color='white'))

# Hide the axis labels
ax.axis('off')

# Show the plot
plt.show()