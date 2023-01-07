#Uniform Distribution

#Importing the necessary libraries.
import timeit 
import random
import numpy as np
import matplotlib.pyplot as plt

#Setting real Pi value as default to find the differences with the estimates I have found.
pi_default = 3.14159265

#Creating empty arrays to save the x, y and difference between the real and estimated Pi values.
array_x = []
array_y = []
differences = []

#Creating a function using Monte Carlo method to estimate Pi value with random numbers.
def estimation_of_pi():
    
    #Setting in_circle and in_square values to 0 at the beginning.
    in_circle = 0
    in_square = 0
    #Creating a loop and running it for 1,000,000 times to find the closest estimate of Pi value.
    for i in range(0, 1000000000):
        
        #Selecting the distribution type.
        x = np.random.uniform()
        y = np.random.uniform()
        
        #Appending x and y values to the arrays.
        array_x.append(x)
        array_y.append(y)
        
        #Calculating the function value according to the function stated in the homework.
        a = (x*x + y*y)**0.5
        
        #If a value is in the circle we increase in_circle by 1, if not we increase in_square by 1.
        if a < 1:
            in_circle += 1
        in_square += 1
        
    #Calculating the Pi value.
    return 4*in_circle/in_square

#Running the function 1000 times to save the results to an array and find the difference between the real and estimated Pi values.
result_array = [estimation_of_pi() for _ in range(1000)]

#For every result in the result_array, we take the difference as absolute value
#and save these values to the differences array.
for j in result_array:
    m = abs(pi_default-j)
    differences.append(m)
    
    #Lastly we take the average of these values.
    o = sum(differences)/len(differences)
    
#Using the generated x and y random values, we plot a histogram chart
#and select the colours and bin values.
plt.hist(array_x, edgecolor="orange", color="purple", bins = 100)
plt.hist(array_y, edgecolor="red", color="pink", bins = 100)

#Adding the labels for the chart.
plt.legend(['X Values', 
            'Y Values'])
plt.title("Uniform Distribution")
plt.xlabel("X and Y Values")
plt.ylabel("Frequency")

#Using the timeit function, we measure the function time to see the difference 
#between Numpy arrays and Python Lists.
print("The time it took for Numpy arrays:", timeit.timeit(stmt = 'estimation_of_pi()', setup = 'from __main__ import estimation_of_pi', number = 1))


#The second version of the code using Python lists

#Uniform Distribution with Python

array_x = []
array_y = []
differences = []

def estimation_of_pi():
    
    in_circle = 0
    in_square = 0
    for i in range(0, 1000000000):
        #The only difference of this version from the first one is this part.
        #I wrote the random number generator using Python features.
        x = random.uniform(0, 1)
        y = random.uniform(0, 1) 
        
        array_x.append(x)
        array_y.append(y)
        
        a = (x*x + y*y)**0.5
        
        if a < 1:
            in_circle += 1
        in_square += 1
        
    return 4*in_circle/in_square

result_array = [estimation_of_pi() for _ in range(1000)]

for j in result_array:
    m = abs(pi_default-j)
    differences.append(m)
    
    o = sum(differences)/len(differences)
    
plt.hist(array_x, edgecolor="orange", color="purple", bins = 100)
plt.hist(array_y, edgecolor="red", color="pink", bins = 100)

plt.legend(['X Values', 
            'Y Values'])
plt.title("Uniform Distribution")
plt.xlabel("X and Y Values")
plt.ylabel("Frequency")

print("The time it took for Python Lists:", timeit.timeit(stmt = 'estimation_of_pi()', setup = 'from __main__ import estimation_of_pi', number = 1))