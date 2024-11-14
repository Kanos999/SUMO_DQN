import os
import pandas as pd
import matplotlib.pyplot as plt

# Directories where episode CSV files for both sets are stored
directory1 = 'outputs/baseline-1'
directory2 = 'outputs/baseline-2'
directory3 = 'outputs/'

# Initialize lists to store the average waiting time per episode for both sets
average_waiting_times_1 = []
average_waiting_times_2 = []

# Function to calculate average waiting times from a directory
def calculate_average_waiting_times(directory):
    average_waiting_times = []
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            # Load the CSV file
            file_path = os.path.join(directory, filename)
            data = pd.read_csv(file_path)
            
            # Calculate the average waiting time for this episode
            avg_waiting_time = data['system_total_waiting_time'].mean()
            average_waiting_times.append(avg_waiting_time)
    return average_waiting_times

# Get average waiting times for both sets
average_waiting_times_1 = calculate_average_waiting_times(directory1)
average_waiting_times_2 = calculate_average_waiting_times(directory2)


data = pd.read_csv('outputs/simulation_results_wait_time.csv')
average_waiting_times_3 = data['system_total_waiting_time']


# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(average_waiting_times_1, marker='o', linestyle='-', label='DQN')
plt.plot(average_waiting_times_2, marker='o', linestyle='-', label='Double DQN')
plt.plot(average_waiting_times_3, marker='o', linestyle='-', label='Our model')
plt.xlabel('Episode')
plt.ylabel('Average System Total Waiting Time')
plt.title('Average System Total Waiting Time Across Episodes')
plt.grid(True)
plt.legend()
plt.show()