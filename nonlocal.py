def make_averager():
    count = 0 
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count
    
    return averager


def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    
    return averager

avg  = make_averager()

try:
    print(avg(10))
except UnboundLocalError as e:
    print(e)

avg  = make_averager2()
print(avg(10))