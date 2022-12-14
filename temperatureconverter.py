#TEMPERATURE CONVERTER BY KINYASH #USE OF TRY AND EXCEPT
x=input("The temperature in degrees celcius (C)?\n")
try:
    print(x)
    y=int(x)
    v =("YOUR TEMPERATURE IN    FAHRENHEIT IS (F)\n")
    print(v)
    o=(y*1.8)+32
    print(o)
    c=(" THE TEMPERATURE IN KELVIN (K)")
    print(c)
    p=273.15+(o-32)*(0.555555555556)
    print(p)
except:
    print('PLEASE TYPE DIGITS ')

    x=input("The temperature in degrees celcius (C)?\n")
    y=int(x)
    v =("YOUR TEMPERATURE IN    FAHRENHEIT IS (F)\n")
    print(v)
    o=(y*1.8)+32
    print(o)
    c=(" THE TEMPERATURE IN KELVIN (K)")
    print(c)
    p=273.15+(o-32)*(0.555555555556)
    print(p)
    quit()
