def filter_duplicates(n):
    p = None
    for i in range(n):
        c = int(input())
        if c != p:
            p = c
            print(p)


input_n = int(input())
filter_duplicates(input_n)
