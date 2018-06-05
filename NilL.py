#--Variables--
A = 5
B = None
C = 0.0039788735772971
#--Pi constant--
pi = 3.14159265359

def calc(A ,B ,C):
    #Checks if A is equal to None while B and C not equal to None
    if(A == None and B != None and C != None):
        r1 = 1/C
        r2 = (2 * pi * B)
        r3 = int(round(r1 / r2))
        return r3
    #Checks if B is equal to None while A and C not equal to None
    elif(B == None and A != None and C != None):
        r1 = 1/C
        r2 = (2 * pi * A)
        r3 = int(round(r1 / r2))
        return r3
    #Checks if C is equal to None while A and B not equal to None
    elif(C == None and A != None and B != None):
        r1 = 1 / 2 (2 * pi * A * B)
        return r1
    else:
        print("Invalid input or more than one parameters are empty")
        
#Print the output of calc()
print(calc(A, B, C))
