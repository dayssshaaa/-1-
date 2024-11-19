import codewars_test as test

def enough(cap, on, wait):
    total_passengers = on + wait
    return max(0, total_passengers - cap)

