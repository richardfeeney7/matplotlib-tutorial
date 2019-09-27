### Import the library and add alias 
import matplotlib.pyplot as plt
import numpy as np 

### Basic Plotting
plt.plot([1,2,3,4]) # List containing numbers
plt.ylabel('Some Numbers')

# Adding label
plt.title("Basic Plot 1")
plt.legend()

plt.show()
 
plt.plot([1,2,3,4], [1,4,9,16]) # Pass two lists (X , Y values)
plt.ylabel("Some Numbers")

# Adding label
plt.title("Basic Plot 2")
plt.legend()

plt.show()

plt.plot([1,2,3,4], [1,4,9,16], "b.") # Pass two lists (X , Y values) removing the line and replace with blue dots
plt.ylabel("Some Numbers")

# Adding label
plt.title("Basic Plot 3")
plt.legend()

plt.show()


#### Two plots on the same Axes + Adding Labels

x = np.arange(0.0, 10.0, 0.01) # All of the values start from 0 to not including 10 with increments of 0.01
y = 3.0 * x + 1.0

noise = np.random.normal(0.0, 1.0, len(x))

plt.plot(x, y + noise, "r", label="Actual") # Plot in red dots + label 
plt.plot(x, y, "b-"       , label ="Model") # Plot in blue + label

# Adding labels
plt.title("Simple Plot")
plt.xlabel("Weight")
plt.ylabel("Mass")
plt.legend()

plt.show()


