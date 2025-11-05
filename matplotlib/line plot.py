import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.plot(x, y, color='blue', linewidth=2, marker='o',markersize=6, label='line plot')

plt.title('Simple line plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.grid(True)
plt.legend()

plt.show()
