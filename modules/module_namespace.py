# module_namespace.py
from matplotlib import pyplot as plt
import random

# namespaces isolate functions, classes, and variables from
# the local namespace, which contains the code you write

# aliasing can prevent conflict when working with modules.

numbers_a = range(1,13)

numbers_b = [random.randint(1,1001) for num in range(0,12)]
print(numbers_b)

plt.plot(numbers_a, numbers_b)

plt.show()