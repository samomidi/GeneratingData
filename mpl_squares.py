import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

plt.title("Square Numbers by Sam", fontsize=24)
plt.xlabel("List Value", fontsize=14)
plt.ylabel("Square of value", fontsize=20)


plt.tick_params(axis='both', labelsize=14)

plt.show()


plt.scatter(2,4)
plt.show()

