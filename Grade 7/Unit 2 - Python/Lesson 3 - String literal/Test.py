Part1Completed = False
choice = 0

print ("This is the text for part 1.")
while Part1Completed == False:
    choice = input()
    if choice.casefold() == "yes":
        Part1Completed = True
    elif choice.casefold() == "no":
        Part1Completed = True
    else:
        print ("Invalid answer, Try Again")

        