A = 5
B = None
C = 0.0039788735772971
pi = 3.14159265359

def calc(A = None , B = None , C = None):
    
    if(A == None and B != None and C != None):
        r1 = 1/C
        r2 = (2 * pi * B)
        r3 = int(round(r1 / r2))
        return r3
    elif(B == None and A != None and C != None):
        r1 = 1/C
        r2 = (2 * pi * A)
        r3 = int(round(r1 / r2))
        return r3
    elif(C == None and A != None and B != None):
        r1 = 1 / 2 (2 * pi * A * B)
        return r1
    else:
        print("Two or more parameters are empty")

print(calc(A, B, C))