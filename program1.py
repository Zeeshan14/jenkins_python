def sumx(x,y):
    z = x + y
    return z

r = sumx(2,5)
f = open("results.txt", "a")
f.write(str(r))
f.close()
