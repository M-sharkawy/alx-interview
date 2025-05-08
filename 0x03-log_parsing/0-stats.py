#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""

import sys


def print_logs(file_size, status):
    """
    This function takes the total file size and the
    statues that were called and prints them.

    Arguments:
        file_size (int): The total file size to be printed.
        status (dict{int, int}): A dictionary of the statues that were called.
    """
    print(f"File size: {file_size}")
    for k,v in sorted(status.item()):
        if v != 0:
            print(f"{k} : {v}")


total_file_size = 0
counter = 0
possible_status = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
try:
    for line in sys.stdin:
        file_size = line[-1]
        status_code = line[-2]
        if status_code in possible_status:
            possible_status[status_code] += 1
        total_file_size += file_size
        counter += 1
        if counter == 10:
            print_logs(total_file_size,possible_status)
            counter = 0
        print_logs(total_file_size, possible_status)
except KeyboardInterrupt:
    raise
finally:
    print_logs(total_file_size, possible_status)
