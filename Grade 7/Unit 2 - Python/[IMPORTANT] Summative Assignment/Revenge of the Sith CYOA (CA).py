#ROTS CYOA By Ahendall
#This is the Complicated Answer (CA) Version

#For the audio to work, You must download simpleaudio through pip
import simpleaudio as sa
import time

from textCA import *
from audio import *



#Actual Code Parts
#Story Part 1
MainTheme()
print(Part1Para)
print("Will you save General Kenobi? (Type: Yes/No)")
Choice1Completed = False
Choice1Ans = 0

while Choice1Completed == False:
    Choice1 = input()
    
    if Choice1.casefold() == "yes":
        print("You have saved General Kenobi!")
        Choice1Ans = 1
        Choice1Completed = True
    
    elif Choice1.casefold() == "no":
        print("You did not save General Kenobi, and he has been killed in action.")
        Choice1Ans = 0
        Choice1Completed = True

    else:
        print ("What you typed isn't an option! Try again.")

# Part 2 Branch 1
if Choice1Ans == 1:
    print(Part2Branch1Para)
    Choice2Completed = False
    Choice2Ans = 0

    while Choice2Completed == False:
        Choice2 = input()
        if Choice2.casefold() == "jedi code":
            print ("You have apprehended an unarmed Count Dooku.")
            Choice2Ans = 1
            Choice2Completed = True
        elif Choice2.casefold() == "chancellor's orders":
            print("You killed Count Dooku.")
            Choice2Ans = 0
            Choice2Completed = True
        else:
            print("What you typed isn't an option! Try again.")
            Choice2Completed = False
    
    #Part 3 Branch 1
    if Choice2Ans == 1:
        print(Part3Branch1Para)

    #Part 3 Branch 2
    if Choice2Ans == 0:
        print(Part3Branch2Para)
        placeholder = input("\n")
        print(Part3ContPara)
        DarthPlagueis()
        print("Will you cut off Windu's Hand or let him kill Palpatine? (Type: Cut Hand/Kill Palpatine)")

        Choice3Ans = 0
        Choice3Completed = False

        while Choice3Completed == False:
            Choice3 = input()

            if Choice3.casefold() == "cut hand":
                Betrayal()
                print("You cut off Mace Windu's Hand!")
                Choice3Ans = 1
                Choice3Completed = True
            
            elif Choice3.casefold() == "kill palpatine":
                Cantina()
                print("You let Master Windu kill Chancellor Palpatine!")
                Choice3Ans = 0
                Choice3Completed = True

            else:
                print ("What you typed isn't an option! Try again.")

        #part 4 branch 1
        if Choice3Ans == 0:
            print(Part4Branch1Para)
            time.sleep(15)
        
        #part 4 branch 2
        elif Choice3Ans == 1:
            print(Part4Branch2Para)
            placeholder = input("\n")
            print(Part4Branch2Cont)
            Choice4Completed = False
            Choice4Ans = 0

            while Choice4Completed == False:
                Choice4 = input()

                if Choice4.casefold() == "kill":
                    print("You have killed the younglings (lmao)!")
                    Choice4Ans = 1
                    Choice4Completed = True

                elif Choice4.casefold() == "spare":
                    print("You have spared the younglings!")
                    Choice4Ans = 0
                    Choice4Completed = True

                else:
                    print("What you typed isn't an option! Try again.")

            #Part 5 Branch 1
            if Choice4Ans == 1:
                print(Part5Branch1Para)
                placeholder = input()
                print(Part5Branch1Cont)
                DontTryIt()
                print(Part5Branch1TryIt)
                Choice5Ans = 0
                Choice5Completed = False

                while Choice5Completed == False:
                    Choice5 = input()

                    if Choice5.casefold() == "try it":
                        print("Uh Oh. Knowing full well Kenobi is the master of the High Ground, you tried it.")
                        Choice5Ans = 1
                        Choice5Completed = True

                    elif Choice5.casefold() == "don't try it":
                        print("You did not try it, and instead retreated.")
                        Choice5Ans = 0
                        Choice5Completed = True

                    else:
                        print("What you typed isn't an option! Try Again.")
            
                #Part 6 Branch 1
                if Choice5Ans == 1:
                    print(Part6Branch1Para)
                    Choice6Ans = 0
                    Choice6Completed = False

                    while Choice6Completed == False:
                        Choice6 = input()

                        if Choice6.casefold() == "hate":
                            print(IHateYou)
                            Immolation()
                            Choice6Ans = 1
                            Choice6Completed = True

                        elif Choice6.casefold() == "silence":
                            print("You stayed silent. Obi Wan watches in sadness as you get engulfed in flames.")
                            Choice6Ans = 0
                            Choice6Completed = True

                        else:
                            print("What you typed isn't an option! Try Again.")

                    #Part 7 Branch 1
                    if Choice6Ans == 1:
                        print(TragicHeroEnding)
                        Deeds()
                        time.sleep(15)

                    #Part 7 Branch 2
                    if Choice6Ans == 0:
                        print(TragicHeroEnding)
                        Deeds()
                        time.sleep(15)

                #Part 6 Branch 2
                if Choice5Ans == 0:
                    Deeds()
                    print(Part6Branch2Para)
                    Choice6Ans = 0
                    Choice6Completed = False

                    while Choice6Completed == False:
                        Choice6 = input()

                        if Choice6.casefold() == "kill":
                            print("You mercilessly killed Palpatine in his sleep.")
                            Choice6Ans = 1
                            Choice6Completed = True

                        elif Choice6.casefold() == "stay":
                            print("You stayed as Palpatine's apprentice!")
                            Choice6Ans = 0
                            Choice6Completed = True

                        else:
                            print("What you typed isn't an option! Try Again.")

                    #Part 7 Branch 3
                    if Choice6Ans == 1:
                        ImpMarch()
                        print(JarJarEnding)
                       
                    #Part 7 Branch 4
                    elif Choice6Ans == 0:
                        print(OverPoweredEnding)

            #Part 5 Branch 2
            elif Choice4Ans == 0:
                ImpMarch()
                print(Part5Branch2Para)
                time.sleep(5)


#Part 2 Branch 2
elif Choice1Ans == 0:
    print(Part2Branch2Para)
