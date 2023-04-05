print("Hello World")

x=5
y=3

print(x**y)
if (x>y):
    print("x is greater")
else: 
    print("y is greater")
x="hi renne!!"

print(x)

friends ={"renne","sam"}
for friend in friends:
    print("hi " + friend)
print(id(friend))

type_var= type(friend)
print(type_var)

for r in range(1,100):
    print(r)

print(globals())

faviort_num=9

def testing_scope():
    x="cat"
    y="dog"
    print("My faviort number is " + str(faviort_num))

testing_scope()

print(6*2-5/(1+4)+3**2)
print(6*2-5/(1+4)+3**2)

disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount= disk_size/sector_size
print(sector_amount) # Should print 33554432.0

def greeting(name):
    print("my name is " + name)

greeting("renne")

a=[1,2]
b=[4,5,8,9,7]
print(a)
for i in a:
    for j in b:
        print(i,j)