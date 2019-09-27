import matplotlib.pyplot as plt #
import numpy as np 


plt.subplot(1, 2, 1) # Will have 1 row with two columns of plots and the final number represents what plot
# 0.0 is the loc parameter and will set the mean of the data
# 1.0 is the scale  and will control the standard deviation of the data. 1 is the default. 
# 10000 is the size and this will control the size and shape of the output
x = np.random.normal(0.0, 1.0, 10000) # Generate random numbers in a bell shaped curve - Center around 0 and push out 1.0 - then i want 10000 of them

# Hist will find the lowest value of x 
plt.hist(x)


plt.subplot(1, 2, 2) # Will have 1 row with two columns
x = np.random.uniform(-3.0, 3.0, 10000) # Uniform generates 10000 numbers between -3 and 3 and any number is as likely as the other 
plt.hist(x)

plt.show()

#### Plot the same as above but instead of side by side have one over the other 

plt.subplot(2, 1, 1)  # Plot 2 rows and 1 column
plt.hist(x)


plt.subplot(2, 1, 2) # Plot 2 rows and 1 column
x = np.random.uniform(-3.0, 3.0, 10000) 
plt.hist(x)

plt.show()


#### Plot the same as above but instead of side by side have one over the other x 3 rows 

plt.subplot(3, 1, 1)  # Plot 3 rows and 1 column
plt.hist(x)


plt.subplot(3, 1, 2) # Plot 3 rows and 1 column
x = np.random.uniform(-3.0, 3.0, 10000) 
plt.hist(x)

plt.subplot(3, 1, 3) # Plot 3 rows and 1 column
x = np.random.uniform(-5.0, 5.0, 10000) 
plt.hist(x)

plt.show()