import sys
import random
import timeit

start = timeit.default_timer() 

name_dict = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
content = ''
end = int(sys.argv[1])

for i in range(0, end*1024):
    content += name_dict[random.randrange(0, 62)];

while(True):
    name = ''

    for i in range(0, 50):
        name += name_dict[random.randrange(0, 62)];

    f = open(name, "w")
    f.write(content)

stop = timeit.default_timer()
print('Time: ', stop - start) 

