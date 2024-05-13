def h(n):
    if n == 1:
        return 1
    else:
        return 1/n + h(n-1)
