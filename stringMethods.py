str = "!!!! this is python basic !!!!!"
str1 = "this is python basic"
str3 = "  "
print(str.upper())
print(str.lower())
print(str.rstrip('!'))
print(str.replace('!','#'))
print(str.split(" "))
print(str1.capitalize())
print(str.center(100))
print(str.count("py"))
print(str1.endswith('sic'))
str2 = str[4:9]
print(str2)
print(str2.endswith('is'))
print (str.endswith('is', 4, 9))

print(str1.find('sa'))
print(str1.index('py'))
print(str.isalnum())
print(str1.isalpha())
print(str.islower())
print(str.isprintable())
print(str3.isspace())
print(str1.istitle())
print(str1.swapcase())
print(str1.title())