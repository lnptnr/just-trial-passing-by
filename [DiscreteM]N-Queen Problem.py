import copy


# Condition Function Set
def condition(x,y) :
    rst = True
    
    for i in range(x+1) :
        if (q[i] == y) or (abs(q[i]-y) == (x+1-i)) : # same column or diagonal = False
            rst = False
            break
    
    return rst

# N-Quuen Function Set
def nq(x,y) :
    global ar
    
    if condition(x,y) :
        q[x+1] = y # x row = y column
        
        if x+1 == n-1 : # last row
            ar += 1
            arlist.append(copy.deepcopy(q)) # add result to arlist
            
        else :
            for col in range(n) :
                nq(x+1,col) # Check next row



# Set
q = [] # Queen Set List
arlist = [] # possible arrangements
ar = 0 # Total possible arrangements

#Input
n = int(input("Enter the number of queens: "))

for i in range(n) :
    q.append(0)
    
# Calculations
for f in range(n) :
    q[0] = f
    
    for c in range(n) :
        nq(0,c)


# Output 1
print("Total possible arrangements:",ar)

# Output 2
print("The first few (not more than 10) arrangments are:")

for a in range(ar) :
    if a > 10 :
        break
    
    for b in range(n) :
        for c in range(n) :
            if arlist[a][b] == c :
                print("1", end = " ")
            else :
                print("0", end = " ")
            
        print()
    
    print()