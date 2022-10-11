def kuusi(k):
    x = 1
    y = ["\n","!",kuusi.__name__,kuusi.__name__[1],"l",kuusi.__name__[2],"o","J"]
    z = "".join(reversed(y))
    for i in range(x-1, k*2, x+1):
        s = " " * (k-x) + "*" * (1 + i * 1) + " " * (k-x) + "\n"
        if 1 + i * 1 == 1: j = s
        z += s
        x += 1
    print(z+j)

kuusi(6)