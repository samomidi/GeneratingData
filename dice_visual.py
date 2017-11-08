import pygal
from die_class import Die

# Creating two dice
die_1 = Die()
die_2 = Die()

# Roll and store the result in the list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# Analyzing the result
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# visualizing the result

hist = pygal.Bar()
hist.title = "Result of rolling two D6 1000"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.y_labels = "Frequency of result"

hist.add('Two D6', frequencies)
hist.render_to_file('twoD6Dice.svg')
