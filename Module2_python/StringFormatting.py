# Method1-Concatenation using + operator
companyName="Ednue technologies"
Suffix=("PVT LTD")

# Method2 -% or C style formatting (for conversion the string into int or round the value)
# %s for string
# %d for integer


name="Moni"
age=20
score=98
print("%s age is %d"%(name,age))
print("%s age is %d.He has scored %.2f in HSC."%(name,age,score))

# Method3 - .format() method
print("{} age is {}.He has scored {} in HSC.".format(name,age,score))
# if change the position pass an argument like{0},{2},{1}
print("{0} age is {2}.He has scored {1} in HSC.".format(name,age,score))

# Method4- 'f'string
personName="Alex"
companyName="Google"
# print(f"{personName} works in {companyName}")   it is not a proper format for f string
print(f"{personName} works in {companyName}")

fruits={
    "apple":10,
    "mango":20
}
print(f"Apple count are {fruits['apple']}")