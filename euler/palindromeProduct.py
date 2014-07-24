from __future__ import division

initial = []
for i in range(1, 100000000):
    for j in range(1,100000000):
        counter = 0
        k  = i*j
        string = str(k)
        numString = list(string)
        if(len(numString)%2 == 0):
            while(counter <= (len(numString)/2)-1):
                if(numString[counter] == numString[len(numString)-1-counter]):
                    if(counter + 1 == len(numString)-1-counter):
                        initial.append(k)
                        break
                    else:
                        counter = counter + 1     
                else:
                    break 
            continue
        else:
            #start from the middle then count out
            for middle in range(len(numString)-1):
                if(middle == len(numString)-1-middle):
                    a = 1
                    while(middle+a <= len(numString)-1):
                        if(numString[middle-a] == numString[middle + a] ):
                            if(middle-a== 0):
                                initial.append(k)
                                break
                            else:
                                a = a+ 1 
                        else:
                            break
                    break
                else:
                    continue 
print (max(initial))