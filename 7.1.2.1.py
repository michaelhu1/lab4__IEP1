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
velocity = data[:, 2]
acceleration = data[:, 3]

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(time, position, label='Position (m)')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(time, velocity, label='Velocity (m/s)', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(time, acceleration, label='Acceleration (m/s²)', color='green')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.title('Acceleration vs Time')
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.show()
