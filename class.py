t=input('WHAT IS THE ROOM TEMP? ')
t=float(t)
t=int(t)
def temp(value):
    if t>=0:
        T=247+(value+t)
        T=str(T)
        return T
    else:
        T=247-(value+t)
        T=str(T)
        return T
print(temp(500)+' .degrees_celcius')