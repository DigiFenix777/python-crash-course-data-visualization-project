# Exercise 15.4 Modified Random Walks
import matplotlib.pyplot as plt

from modified_random_walk import ModRandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = ModRandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.inferno,
               edgecolors='none', s=1)
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Print plot to screen
    # plt.show()
    # Save plot to file.
    plt.savefig('mod_random_walk_inferno_02.png', bbox_inches='tight')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
