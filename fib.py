'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

def produceFibsList(n):
    fib_list = []

    for i in range(0, n):
        if i < 2:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[i-1] + fib_list[i-2])

    return fib_list

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    n = int(input("Input n: "))
    print(produceFibsList(n))
