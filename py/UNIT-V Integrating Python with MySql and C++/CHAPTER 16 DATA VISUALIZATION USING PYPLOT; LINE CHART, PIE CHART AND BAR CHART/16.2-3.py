import matplotlib.pyplot as plt
x=[1,2,3]
y=[5,7,4]
x2=[1,2,3]
y2=[10,14,12]
plt.plot(x,y,label='Line 1')
plt.plot(x2,y2,label='Line 2')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('LINE GRAPH')
plt.legend()
plt.show()
