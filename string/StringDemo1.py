data = "python is programming lang"
print(data)
print(data[0])

#data[0] = "P" #TypeError: 'str' object does not support item assignment
#print(data)

#how to find length...

x = len(data)
print("len of string is ",x)

# for i in range(0,len(data)):
#     print(data[i],end="")

#foreach

for i in data:
    print(i,end="")
