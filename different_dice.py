from die_class import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(5000):
    total = die_1.roll() + die_2.roll()
    results.append(total)

print(results)

# Analyzing the rolls
frequencies = []
max_value = die_2.num_sides + die_1.num_sides
for value in range(2, max_value + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# visualizing result

hist = pygal.Bar()
hist.title = "Result of rolling a D6 and D10"
hist.x_title = "Result"
hist.y_title = "Frequency of result"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

hist.add("D6 and D10", frequencies)
hist.render_to_file('D6AndD10Dice.svg')
