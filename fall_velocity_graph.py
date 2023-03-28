import matplotlib.pyplot as plt
mass = 68.1
gravity_acc = 9.81
drag_coeff = 12.5
step = 2
dvdt = gravity_acc
velocities = [0]
times = [0]

while dvdt > 0.1:
    dvdt = gravity_acc - ((drag_coeff * velocities[-1]) / mass)
    velocities.append(velocities[-1] + dvdt * step)
    times.append(times[-1] + step)

plt.plot(times, velocities, 'b--o')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()