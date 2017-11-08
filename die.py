from random import randint
import pygal
from die_class import Die


my_die = Die()
print(my_die.roll())

dice_list = []
for die in range(1000):
    # dice_list.append(randint(1, my_die.num_sides))
    dice_list.append(my_die.roll())
print(dice_list)

# Analyzing the result, how many each number appeared
frequencies = []
for value in range(1, my_die.num_sides+1):
    frequency = dice_list.count(value)
    frequencies.append(frequency)
print(frequencies)

index = 0
for freq in frequencies:
    index += 1
    print("Number " + str(index) + " has repeated for " + str(freq) + " times")

hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '5']
hist.y_labels = "Frequency of result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')