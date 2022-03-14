import math

def findMaxScore(a, b):
    N = int(a[0])
    K = int(a[1])
    num_iter = math.ceil(N/K) #the number of possible arrangement for this specific N and K
    remainder = N%K #this indicate if N can be completely devided by K
    #if yes, remainder ==  0
    #then there will only be one possibility 
    i = 0 #keep track of the process of num_iter
    glb_max = 0
    while i < num_iter: #ala num_iteration do not go over the possibilities
        j = 0
        lcl_max = 0
        ini = i * K 
        while j < len(b):
            if j == ini and remainder != 0: 
                lcl_max += int(max(b[ini: ini+remainder], key=int))
                j += remainder
                continue
            else:
                lcl_max += int(max(b[j: j+K], key=int))
            j += K
        glb_max = max(glb_max, lcl_max)
        i += 1 #the i is more like how many while loop it has experience?
        if (remainder == 0):
            break
    return glb_max

fp=open("S4\s4.3-36.in")

a = fp.readline().split(" ")

b = fp.read().strip().split(" ")


result = findMaxScore(a, b)
#print(a)
#print(b)
print(result)
