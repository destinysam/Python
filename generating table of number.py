import sys

def table(a):
    for i in range(1,11):
        print(f"{a} * {i} = {a*i}")


table(int(sys.argv[1]))
