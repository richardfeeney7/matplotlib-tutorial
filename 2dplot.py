# Import the library and add alias 
import matplotlib.pyplot as plt

plt.plot([1,2,3,4]) # List containing numbers
plt.ylabel('Some Numbers')
plt.show()
 
plt.plot([1,2,3,4], [1,4,9,16]) # Pass two lists (X , Y values)
plt.ylabel("Some Numbers")
plt.show()

plt.plot([1,2,3,4], [1,4,9,16], "b.") # Pass two lists (X , Y values) removing the line and replace with blue dots
plt.ylabel("Some Numbers")
plt.show()