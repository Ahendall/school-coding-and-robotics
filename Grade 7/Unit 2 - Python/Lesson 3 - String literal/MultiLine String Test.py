# SELF NOTE: Use casefold() for the case-sensitive matching
# SELF NOTE: upper() and lower() also work just fine but eh whatever

choice = 0
print ('''
You are General Anakin Skywalker During the battle above Coruscant.

You are on the way to Seperatist General Grievous' ship.
Your master, General Kenobi, has had his Starfighter hit by buzz droids

Will you save him?
(Type: yes | no)
''')

choice = input()

if choice.casefold() == "yes":
    print ("You have saved General Kenobi!")
elif choice.casefold() == "no":
    print ("General Kenobi has been killed in action.")
