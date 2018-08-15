import matplotlib.pyplot as plt

class plot_item():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

filename = "C:\Users\yoav.e\Desktop\Airties\ATA-3\performance\performance-loadpercentage.txt"
with open(filename, 'r') as file:
    all_data = file.read()

my_data = [item for item in all_data.split('\n') if item.__contains__('result')]
ready_data = []
for item in my_data:
    x = item.split(' operation')[0]
    y = item.split('=')[1].split('\r\r')[0]
    temp_plot_item = plot_item(x, y)
    ready_data.append(temp_plot_item)

# reduce data
reduced_data = []
for i,item in enumerate(ready_data):
    if i != 0:
        try:
            if int(item.y) > int(ready_data[i-1].y)+5 or int(item.y) < int(ready_data[i-1].y)-5:
                reduced_data.append(item)
        except Exception as e:
            pass

all_x = [item.x.split('-')[2] for item in reduced_data]
all_y = [int(item.y) for item in reduced_data]

plt.plot(all_x, all_y)

plt.xlabel('time (s)')
plt.ylabel('running executions')
plt.title('running executions over time')
plt.grid(True)
plt.savefig("test.png")
plt.show()

