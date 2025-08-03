#RK 4th order method

def g(x,y,z):
    return  x*(z**2) - (y**2)

def RK():
    x,y,z =[],[],[]
    h = float(input("height : "))
    x0 = float(input("X0 : "))
    y0 = float(input("y0 : "))
    z0 = float(input("Z0 : "))
    req_x = float(input("req x : "))
    x.append(x0)
    y.append(y0)
    z.append(z0)

    n = int(req_x/h)

    for i in range(n):
       
        m1 = z[i]
        p1 = g(x[i],y[i],z[i])
        m2 = z[i] + (p1/2)
        p2 = g( x[i] + h/2, y[i] + m1/2, z[i] + p1/2)
        m3 = z[i] + p2/2
        p3 = g(x[i] + h/2, y[i] + m2/2, z[i] + p2/2)
        m4 = z[i]+p3
        p4 = g(x[i] + h, y[i] + m3, z[i] + p3)

        x_new = x[i] + h
        y_new = y[i] + (h/6)* (m1 + 2*m2 + 2*m3 + m4)
        z_new = z[i] + (h/6)* (p1 + 2*p2 + 2*p3 + p4)

        x.append(x_new)
        y.append(y_new)
        z.append(z_new)

    print(f"\n x = {x} \n y = {y} \n z = {z}")

RK()