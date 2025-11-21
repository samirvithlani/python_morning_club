name = "jay"
print(name.isupper())
print(name.islower())

name = "Hi Hello"
print(name.istitle())

name = "a-z"
print("alnum",name.isalnum())

name = "raj" #[a-zA-z]
print(name.isalpha())

name = "123"
print(name.isdigit())
#print(name.isnumeric())

data ="" #blnk

print("printable ...",data.isprintable())

email ="samir@gmail.com"
#print(email.startswith("x"))
print(email.startswith("@",5))
print(email.endswith("c",10,13))

