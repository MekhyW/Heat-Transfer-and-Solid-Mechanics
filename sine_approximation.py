import math
x = float(input("Enter the value of x: "))
precision = float(input("Enter the precision: "))

previous_approx = 0.00000001
current_approx = x
i = 1

while (abs((current_approx - previous_approx)/previous_approx)) > precision:
    i += 1
    previous_approx = current_approx
    current_approx += ((-1)**(i+1))*(x**(2*i-1))/math.factorial(2*i-1)

print("The approximation is: ", current_approx)
print("Terms used: ", i)