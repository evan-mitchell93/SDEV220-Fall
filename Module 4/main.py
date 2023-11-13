
import random
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
combo = dict(enumerate(months,start=1))

def my_square(x):
    return x ** 2

my_map = list(map(my_square, [1,2,3,4]))
print(random.choice(my_map))