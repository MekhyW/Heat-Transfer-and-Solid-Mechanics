import matplotlib.pyplot as plt
lenght = 10
step_x = 2
step_t = 0.1
thermal_diffusivity = 0.835
number_of_nodes = int(lenght / step_x)
temperature = [100] + [0]*(number_of_nodes-1) + [50]
t_max = 9

for t in range(0, int(t_max*10), int(step_t*10)):
    print(temperature)
    temperature_prev = temperature.copy()
    for i in range(1, number_of_nodes):
        temperature[i] = temperature_prev[i] + (thermal_diffusivity * step_t * (temperature_prev[i+1] - 2*temperature_prev[i] + temperature_prev[i-1]) / step_x**2)
    
plt.plot(range(0, lenght+step_x, step_x), temperature, 'b')
plt.xlabel('Position (m)')
plt.ylabel('Temperature (C)')
plt.show()