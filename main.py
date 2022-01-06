import sys
import getopt
import re
import statistics
from collections import Counter


def print_help():
    # TODO help
    print('Help')


def process_file(path: str):
    with open(path, 'r') as ping_file:
        times = []
        not_processed = []
        for row in ping_file:
            if row != '\n':
                ping_time = re.search(r'time=(\d*)', row)
                if ping_time:
                    times.append(int(ping_time.group(1)))
                else:
                    if re.search(r'Request timed out', row):
                        times.append(-1)
                    not_processed.append(row)
        counted_times = Counter(times)
        print(f'total number of records - {sum(counted_times.values())}')
        print('ping below 200\t:\t{0}'.format(
            sum(count for ping_time, count in counted_times.items()
                if ping_time <= 100))
        )
        print('ping over 200\t:\t{0}'.format(
            sum(count for ping_time, count in counted_times.items()
                if ping_time > 100))
        )
        print(f'min ping\t\t:\t{min(times)}' + '\n'
              + f'max ping\t\t:\t{max(times)}' + '\n'
              + f'mean ping\t\t:\t{statistics.mean(times)}')


def ping():
    # TODO make ping analyzing in real time
    pass


def main():
    arg_list = sys.argv[1:]
    short_options = "hf:p:v"
    long_options = ['help', 'file', 'ping', 'visualise']
    try:
        arguments, values = getopt.getopt(arg_list, short_options,
                                          long_options)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)
    for argument, value in arguments:
        if argument in ['-h', '--help']:
            print_help()
        elif argument in ['-f', '--file']:
            process_file(value)
        elif argument in ['-p', '--ping']:
            ping()


if __name__ == '__main__':
    main()
