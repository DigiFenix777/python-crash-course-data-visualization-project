import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(5000)  # Use 5000 points as requested
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the path of the walk
ax.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)

# Plot the starting and ending points
ax.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)  # Start point
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100, zorder=2) # End point

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()