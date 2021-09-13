# name = "Elvis"
# jobTitle = "Instructor"

#Formatting Strings

#Concatenation
# solution1 =  name + " is an " + jobTitle
#print(solution1)
# solution2 = name * 5
# print(solution2)

#Appending: You are Concatenating AND Assigning at the same
#Equivalent in Concatenation: 
    #name = name + jobTitle
#name += jobTitle


    #name -> ElvisInstructor
# name += jobTitle
#     #name -> Elvis
#     #jobTitle -> Instructor
#     #+= -> Append
#         # FIRST: name + jobTitle
#         #SECOND: name = name + jobTitle

#print(name)

#Escape Sequences: 
    #\n -> New Line 
    #\t -> HORIZONTAL tab space
    #\v -> VERTICAL tab space
# sentence = "Elvis, \n \v Is the greatest... \t OF ALL TIME!"
#print(sentence)


#Argument by Position
# solution4 = "My lucky number {0} and my name is".format("Elvis")
# Using a double pair of brackets will display a single '{}'

#print(solution4)

#Argument by Name/Reference
# solution5 = "My name is {name}".format(name="Elvis")
#print(solution5)

#Student Response Hybrid: Argument by Position AND Reference/Name
#demo = 3
#solution6 = "My name is {1} and my favorite number is {number} and I am working as an {job}".format(demo, number=9,job="Instructor", name="Tyler", name2="Elvis")
#print(solution6)


#F-Strings
'''
age = 27
isWorking = True

print(f"My name is {name} and I am {age} and currently am I working?: {isWorking}, what do I do for a living: {jobTitle}")
'''

#String Methods: 

#Method #1: .capitalize()
    #Python is an Object Oriented Language. EVERYTHING is an object. 
    #Objects have 2 things: 
        #1. Properties (Props)
        #2. Behavior: Capitalizes the FIRST letter of a String only.  

'''
name = "elvis garcia"



print(name.capitalize())

print(name)

'''

#Method #2: .upper()
    #Behavior: Capitalizes ALL characters/letters in your string. 
name = 'elvis garcia'
print(name.upper())

#Method #3: .lower()
    #Behavior: Lowercases ALL characters/letters in your string.

# print("eLvIs GaRcIa".lower().capitalize())
# print("Elvis GaRcIa".lower().capitalize())

#Method 4: .swapcase()
    #Behavior: Flips Lower to Upper and Upper to Lower
    #I.P.O: Input Processing Output
    #Input: String
    #Process: len()
    #Output: Number/Integer

name2 = "elvis garcia"
print(name2.swapcase())

#Method 5: len()
    #Example: Structure 1: Object.method() 
              #Structure 2: method(Object)

print(len(name2))

print(type(name2))







