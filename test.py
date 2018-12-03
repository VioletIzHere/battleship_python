import time

c = 0
while True:
    p = str(int(11**c))
    np = ""
    for l in p:
        np += l + " "
    print(np)
    c += 1
    time.sleep(0.2)