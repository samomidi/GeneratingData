from random import choice

class RandomWalk():

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # All walks starts at (0.0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            # x_direction = choice([1])
            x_distance = choice([0, 1, 2, 3, 4])
            # x_distance = choice(list(range(1,20)))
            x_step = x_direction * x_distance

            # y_direction = choice([1])
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4., 5])
            y_step = y_direction * y_distance

            if x_step and y_step == 0:
                continue

            # calculate next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

import matplotlib.pyplot as plt

# while True:

rw = RandomWalk(10000)
rw.fill_walk()
plt.figure(dpi=128, figsize=(10, 6))
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, s=5, edgecolors='none', c=point_numbers, cmap=plt.cm.Blues)

# plt.scatter(rw.x_values, rw.y_values, s=5, edgecolors='none', c=rw.x_values, cmap=plt.cm.Blues)
# plt.plot(rw.x_values, rw.y_values)

# Showing the first and last point
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

#Remove the axes
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# set the size of the plotting window


plt.show()

    # keep_running = input("Continue with another walk?(y/n)")
    # if keep_running == ('n' or 'N'):
    #     break

