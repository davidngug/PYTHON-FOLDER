fruit='banana'
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1
a=' hello'
b=a+' there '
print(b,1.0)
y=len(fruit)
y=str(y)
print('letters are '+ y,2.0)
b=b.upper()#upper is used to convert to capital letters 
print(b,3.0)
b=b.lower()#lower is used to convert to small
print(b,4.0)
f=b.find('lo')#find is used to find start of index of a search ,if search is not found returns index value as -1
print(f,5.0)
b=b.replace('hello','fello')#replaces every word(hello) in variable
print(b,6.0)
b=b.capitalize()#Turns first letter to capital in variable
print(b,7.0)
print(b.lstrip(),8.0)#Removes space on left

print(b.rstrip(),9.0)#removes space on right, refer 4.2Class.py
 
print(b.strip(),10.0)#removes spaces generally infront nd back

print(b.startswith(' fello'),11.0)#confirms variable starts with a specific str/int ( fello)

print(b.endswith('there '),12.0)#confirms variable ends with a specific str/int (there )
print(b.endswith('f'),13.0)#EXAMPLE

print(b.split(),14.0)#changes a group of strings to a list using spaces
s=('willow;jayson;phillips')#EGXAMPLE
print(b.split(';'))#Can be used to seperate a bunch of strings to list using [;] but specifying can use any even if its a [/][,][.]
quit()