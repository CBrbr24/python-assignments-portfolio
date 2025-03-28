x = 0.5
i= 0
b = 0
n = 26
funtanround = 0
funtanrounderr = 0
funtan = 0
funtanerr = 0

if (x < 0) or (x > 1):
    print("error")
    #Checks that x is between 0 and 1

else:
    for i in range(n-1):
     funtanround = funtanround + funtan
#adds each round of calculation to previous sum
     funtan = (((-1)**i)*((x)**(2*1)+1))/((2*i)+1)
#Actual calculation
    i= i+1
    for b in range(n-1):
        funtanrounderr = funtanrounderr + funtanerr
        funtanerr = (((-1) ** b) * ((x) ** (2 * 1) + 1)) / ((2 * b) + 1)
        b = b + 1
#Checks error
error = funtanround - funtanrounderr
if error <= ((x**((2*n)+1))/((2*n)+1)):
        print (funtanround,n,error)