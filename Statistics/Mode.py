from collections import Counter


def mode(num):
    try:
        num_values = len(num)
        count = Counter(num)
        find_mode = dict(count)
        mode = [k for k, v in find_mode.items() if v == max(list(count.values()))]
        if len(mode) == num_values:
            find_mode = "No mode found"
        else:
            find_mode = mode[0]
        return find_mode
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print('Error: Check your data inputs')
