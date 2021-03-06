#working with strings
print("hello world")
print("python says" + ' ' + "hello world")
print("hello\nworld")
print("hello\"world")
print("hello\world")

#using functions 
a = "hello world"
print(a)
print("python says" + ' ' + a)
print(a.upper())
print(a.lower())
print(a.upper().isupper())
print(a.count(a))
print(len(a))
print(a[3])
print(a.index("w"))
print(a.index("world"))
print(a.replace('o','a'))
print(a.swapcase())
print(a.lstrip())
print(a.capitalize())
print(a.startswith("h"))
print(a.startswith("v"))
print(a.endswith("d"))
print(a.endswith("r"))
print(a.casefold())
print(a.find("r"))
print(a.rstrip())
print(a.strip())
print(a.split())
print(a.title())
print(a.translate(a))
print(a.rfind("r"))
print(a.rindex("o"))
print(a.index("o"))
print(a.rsplit())
print(a.istitle())
print(a.title().istitle())
print(a.partition("r"))
print(a.format())
print(a.splitlines())
print(a.join(a))
print(a.join("r"))
print(a.ljust(1))
print(a.rjust(1))
print(a.isnumeric())
print(a.isspace())
print(a.isalpha())
print(a.isalnum())
print(a.isdecimal())
print(a.isdigit())
print(a.format_map(a))
