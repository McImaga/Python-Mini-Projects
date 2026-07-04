import numpy as np
import matplotlib.pyplot as plt

# 1. Define the functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

# 2. Create data from -20 to 10
x = np.linspace(-20, 10, 400) 

# 3. Calculate y values
y_sig = sigmoid(x)
y_tanh = tanh(x)
y_relu = relu(x)

# 4. Plot all 3
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x, y_sig, color='blue')
plt.title('Sigmoid: 1/(1+e^-x)')
plt.axhline(0, color='black', lw=0.5); plt.axvline(0, color='black', lw=0.5)
plt.ylim(-0.1, 1.1)

plt.subplot(1, 3, 2)
plt.plot(x, y_tanh, color='red')
plt.title('Tanh: (e^x - e^-x)/(e^x + e^-x)')
plt.axhline(0, color='black', lw=0.5); plt.axvline(0, color='black', lw=0.5)
plt.ylim(-1.1, 1.1)

plt.subplot(1, 3, 3)
plt.plot(x, y_relu, color='green')
plt.title('ReLU: max(0, x)')
plt.axhline(0, color='black', lw=0.5); plt.axvline(0, color='black', lw=0.5)
plt.ylim(-1, 11)

plt.tight_layout()
plt.savefig('activation_functions.png', dpi=150) # Save for README
plt.show()