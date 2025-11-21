#string[start:end:step]

#012345
#-6-5-4-3-2-1
s = "PYTHON"
print(s[0:6])
print(s[:6])
#print(s[7:12])
print(s[:])

#negative slicing
print(s[-4:])
print(s[-6:-3])

#step values
s = "PYTHON PROGRAMMING"
print(s[9:1:2])
#skip start skip end
#0   end   step 2
print(s[::2])
print(s[::-1])

#print(s[9000]) error