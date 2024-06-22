S = "Chenchu Gokul Jangam"
str = "Gokul Jangam"
#printing indexing
print(S[2])
print(S[0])
print(S[7])
print(str[-1])
print(str[-5])

#slicing
#[start:stop]
print(S[1:3]) #print numbers before stop value
print(S[:5]) #print numbers before stop value
print(S[:-1]) #print numbers before stop value
print(S[1:-2]) 
print(S[2:]) # printing values from start value to total
print(S[-9:]) # printing values from start value to total

#start:stop:step
print(str[::2])  #steping the number band printing the numbers by jumping
print(str[3::2])  #steping the number band printing the numbers by jumping
print(str[::-1])  #printng numbers in revese
print(str[-8::-1])  #printng numbers in revese from strt num
print(str[8::-1])  #printng numbers in revese from start num