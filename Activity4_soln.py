firstName= "Elvis"
lastName = "Garcia"
favoriteMeal = "Spanish Food/Dominican Food"
favoriteColor = "Violet"

#F-Strings
'''
print(f"My first name is {firstName} my last name is {lastName} my favorite meal is {favoriteMeal} and my favorite is {favoriteColor}")
'''

#Argument by name:
'''
solution = "My first name is {a} my last name is {b} my favorite meal is {c} and my favorite color is {d}".format(b="Garcia", d="Blue", a="Elvis", c="Mangu")
print(solution)
'''


#Argument by position: 
#   #When you're counting positioning. YOU START COUNTING AT 0. 
'''
solution2 = "My first name is {0} my last name is {1} my favorite meal is {2} and my favorite color is {3}".format("Elvis", "Garcia", "Mangu", "Purple")
'''

#Concatenation: 
'''
solution3 = "My first name is " + firstName + " my last name is " + lastName + " my favorite meal is " + " Mangu " + "my favorite color is " + " Orange."
print(solution3)
'''


#Hybrid Model: Argument by Name and Position: 
age = 27
numOfCryptosOwned = 15
solution4 = "I am {0} years old, and I am {e}, and I own like {1} cryptocurrencies".format(age, numOfCryptosOwned, e="Latino")
print(solution4)