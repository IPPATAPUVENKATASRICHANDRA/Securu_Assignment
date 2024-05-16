import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to fetch data from the server
def fetch_data():
    response = requests.get('http://localhost:5000/system-info')
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return None

# Function to update the plot
def update_plot(frame):
    data = fetch_data()
    if data:
        x.append(frame)
        cpu_y.append(data['cpu_usage'])
        memory_y.append(data['memory_usage'])
        disk_y.append(data['disk_usage'])
        plt.cla()
        plt.plot(x, cpu_y, label='CPU Usage')
        plt.plot(x, memory_y, label='Memory Usage')
        plt.plot(x, disk_y, label='Disk Usage')
        plt.xlabel('Time')
        plt.ylabel('Usage (%)')
        plt.title('Real-Time System Usage')
        plt.legend()
        plt.grid(True)

        if len(x) > 20:
            x.pop(0)
            cpu_y.pop(0)
            memory_y.pop(0)
            disk_y.pop(0)

# Initialize lists to store data
x = []
cpu_y = []
memory_y = []
disk_y = []

# Set up the plot
plt.style.use('ggplot')
fig = plt.figure()
ani = FuncAnimation(fig, update_plot, interval=1000)  # Update plot every second
plt.show()
