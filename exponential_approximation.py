import math
exponent = float(input("Enter the exponent: "))
precision = float(input("Enter the precision: "))

previous_approx = 1
current_approx = 1 + exponent
i = 1

while (abs((current_approx - previous_approx)/previous_approx)) > precision:
    i += 1
    previous_approx = current_approx
    current_approx += (exponent**i)/math.factorial(i)

print("The approximation is: ", current_approx)
print("Terms used: ", i)