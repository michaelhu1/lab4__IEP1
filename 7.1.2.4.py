import numpy as np
import matplotlib.pyplot as plt

def preprocess_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    processed_lines = []
    for line in lines:
        processed_lines.append(line.replace(',,', ',NaN,').replace(',\n', ',NaN\n').replace('\n', ',NaN\n'))

    with open('processed_data.csv', 'w') as processed_file:
        processed_file.writelines(processed_lines)

    return 'processed_data.csv'

preprocessed_file = preprocess_file('lab1_data.csv')

data = np.loadtxt(preprocessed_file, delimiter=',', skiprows=1)

time = data[:, 0]
position = data[:, 1]
capstone_velocity = data[:, 2]  
capstone_acceleration = data[:, 3]  

Delta_t = time[1] - time[0]

#assuming uncertainty in position. can be changed
delta_x = 0.001 

velocity = np.zeros(len(time) - 2)
velocity_uncertainty = np.zeros(len(time) - 2)
acceleration = np.zeros(len(time) - 2)
acceleration_uncertainty = np.zeros(len(time) - 2)

for i in range(1, len(time) - 1):
    velocity[i - 1] = (position[i + 1] - position[i - 1]) / (2 * Delta_t)
    velocity_uncertainty[i - 1] = np.sqrt(2) * delta_x / (2 * Delta_t)

    acceleration[i - 1] = (position[i + 1] - 2 * position[i] + position[i - 1]) / (Delta_t ** 2)
    acceleration_uncertainty[i - 1] = np.sqrt(6) * delta_x / (Delta_t ** 2)


time_calculated = time[1:-1]  

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(time, position, label='Position (m)')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.errorbar(time_calculated, velocity, yerr=velocity_uncertainty, label='Calculated Velocity', fmt='o', capsize=3, color='blue')
plt.plot(time, capstone_velocity, label='Capstone Velocity', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Comparison of Calculated Velocity and Capstone Velocity')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.errorbar(time_calculated, acceleration, yerr=acceleration_uncertainty, label='Calculated Acceleration', fmt='o', capsize=3, color='green')
plt.plot(time, capstone_acceleration, label='Capstone Acceleration', color='red')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.title('Comparison of Calculated Acceleration and Capstone Acceleration')
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.show()
