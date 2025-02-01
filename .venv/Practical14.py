import matplotlib.pyplot as plt
import numpy as np

# Generate data for plotting
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a basic line plot
plt.figure()
plt.plot(x, y, label='sin(x)', color='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Line Plot')
plt.legend()
plt.grid()
plt.show()

# Create a scatter plot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
plt.figure()
plt.scatter(x_scatter, y_scatter, color='red', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.grid()
plt.show()

# Create a bar chart
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 1, 5]
plt.figure()
plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()

# Create a histogram
data = np.random.randn(1000)
plt.figure()
plt.hist(data, bins=30, color='cyan', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
