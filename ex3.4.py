def LastNlines(fname, N):
    with open(fname) as file:
        for line in (file.readlines() [-N:]):
            print(line)


fname = 'test.txt'
N = 5
try:
    LastNlines(fname, N)
except:
    print('File not found')
