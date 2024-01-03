#for i in range (4):
#    print ("Wahyu")

#for i in range (10, 0, -2):
#    print (i)

#for i in range (0, 10, 2):
#    print (i)

#for i in range (1,11):
#    for j in range (1,11):
#        k=i*j
#        print (k, end="")
#    print ()

#i = 1
#while i<6:
#    print (i)
#    if i==3:
#        break
#    i+=1

#i = 0
#while i<6:
#    i+=1
#    if i==3:
#        continue
#    print(i)

print("No.1")
print()

n = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 
    980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 
    263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 
    942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 
    823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 
    758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 
    626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 
    892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 
    717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 
    857, 440, 380, 126, 721, 328, 753, 470, 743, 527
]
a = 0

while a < len (n):
    if(n[a] % 2 != 0):
        print(n[a])
    if(n[a]==553):
        break
    a+=1

print()
print("No.2")
print()

a=1
b=0
while (a <20):
    print(a, end=" + ")
    b+=a
    a+=2
print(a,"=",b)

print()
print("No.3")
print()

for i in range (0,10):
    for b in range (0,10):
        if i > b:
            print("*", end="")
    print()