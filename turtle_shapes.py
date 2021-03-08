def square(t, size):
    t.pd()
    t.seth(0)
    for i in range(4):
        t.fd(size)
        t.rt(90)

def tri(t, size):
    t.pd()
    t.seth(60)
    for i in range(3):
        t.fd(size)
        t.rt(120)