print('1-------------')
'''
import matplotlib.pyplot as plt

# plt.scatter(2,4, s=200)
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values,y_values, s=100)


plt.title("Square Numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("square of values", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
'''
print('2-------------')

import matplotlib.pyplot as plt

x_values = list(range(1, 1001)) # 1 to 1000
y_values = [x**2 for x in x_values]
# y_values = []
# for x in x_values:
#     y_values.append(x)

plt.scatter(x_values, y_values, edgecolors='none', c=x_values, cmap=plt.cm.Blues, s=1)
# plt.scatter(x_values, y_values, edgecolors='none', c=(1,0,1), s=1)
# plt.scatter(x_values, y_values, edgecolors='none', c='red', s=1)

plt.title("Square number 1 to 1000")
plt.xlabel("square value", fontsize=14)
plt.ylabel("Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.savefig('square_plot.png', bbx_inches='tight')
plt.show()
