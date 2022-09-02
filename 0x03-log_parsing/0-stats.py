#!/usr/bin/python3
"""Log parsing"""
import sys


def read():
    """reading of each line that enters the system"""
    read = sys.stdin.read().split('\n')
    return read


def recorrer():
    """loop through the entire data array"""
    cont = 0
    result = {}
    sum = 0
    try:
        for item in read():
            for status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                metrics = item.split(' ')
                try:
                    if(metrics[7] == str(status_code)):
                        if (result.get(status_code) is None):
                            result[status_code] = 1
                        else:
                            result[status_code] = result.get(status_code) + 1
                        sum += int(metrics[8])
                        cont += 1
                except Exception:
                    pass

            if (cont == 10):
                print_result(result, sum)
                cont = 0
    except KeyboardInterrupt:
        pass

    print_result(result, sum)


def print_result(result, sum):
    """print the information according to a format"""
    if(result):
        print("File size: {}".format(sum))
        for key, value in sorted(result.items()):
            print("{}: {}".format(key, value))

if __name__ == "__main__":
    recorrer()
