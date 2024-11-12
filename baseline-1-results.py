import os
import pandas as pd
import matplotlib.pyplot as plt

# Directory where all episode CSV files are stored
directory = 'outputs/intersection_DoubleDQN'

# Initialize a list to store the average waiting time per episode
average_waiting_times = []

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Load the CSV file
        file_path = os.path.join(directory, filename)
        data = pd.read_csv(file_path)
        
        # Calculate the average waiting time for this episode
        avg_waiting_time = data['system_total_waiting_time'].mean()
        average_waiting_times.append(avg_waiting_time)

# Plot the average system_total_waiting_time across episodes
plt.figure(figsize=(10, 6))
plt.plot(average_waiting_times, marker='o', linestyle='-')
plt.xlabel('Episode')
plt.ylabel('Average System Total Waiting Time')
plt.title('Average System Total Waiting Time Across Episodes')
plt.grid(True)
plt.show()
