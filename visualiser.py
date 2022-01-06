import re
import matplotlib.pyplot as plt
import os


def visualise(paths: list, res_folder_name: str) -> None:
    data = []
    for path in paths:
        with open(path) as file_with_ping_info:
            for row in file_with_ping_info:
                ping_time = re.search(r'(?:time=)(\d*)', row)
                if ping_time:
                    data.append(int(ping_time.group(1)))
                elif re.search(r'Request timed out', row):
                    data.append(-100)
    diapason = 1000
    try:
        os.makedirs(res_folder_name)
    except OSError:
        pass
    min_ping = min(data)
    max_ping = max(data)
    for x in range(0, len(data), diapason):
        plt.figure(figsize=(19.2, 10.8))
        plt.ylim(min_ping, max_ping)
        current_data = data[x:x + diapason]
        x_range = x + len(current_data)
        plt.plot([_ for _ in range(x, x_range)], current_data)
        plt.savefig(f'{res_folder_name}/ping_range_from{x}to{x_range}.png')
        plt.close()
