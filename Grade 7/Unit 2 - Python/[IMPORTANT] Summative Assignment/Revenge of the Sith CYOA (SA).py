"""
ROTS CYOA By Ahendall
This is the Simple Answer (SA) Version.
This is exactly the same as the CA Version but easier to answer.
"""
# For the audio to work, You must download simpleaudio through pip
import simpleaudio as sa
import time

from textSA import *
from audio import *


# Actual Code Parts
# Story Part 1
MainTheme()
print(Part1Para)
print(
    "To save Keneral Kenobi, type the number 1.\n"
    + "To let his ship get destroyed by buzz droids, type 2."
)
Choice1Completed = False

while Choice1Completed == False:
    Choice1 = input()

    if Choice1 == "1":
        print("You have saved General Kenobi!")
        Choice1Completed = True

    elif Choice1 == "2":
        print("You did not save General Kenobi, and he has been killed in action.")
        Choice1Completed = True

    else:
        print("What you typed isn't an option! Try again.")

# Part 2 Branch 1
if Choice1 == "1":
    print(Part2Branch1Para)
    Choice2Completed = False

    while Choice2Completed == False:
        Choice2 = input()
        if Choice2 == "2":
            print("You have apprehended an unarmed Count Dooku.")
            Choice2Completed = True

        elif Choice2 == "1":
            print("You killed Count Dooku.")
            Choice2Completed = True

        else:
            print("What you typed isn't an option! Try again.")
            Choice2Completed = False

    # Part 3 Branch 1
    if Choice2 == "2":
        print(Part3Branch1Para)
        time.sleep(15)
        sa.stop_all()

    # Part 3 Branch 2
    if Choice2 == "1":
        print(Part3Branch2Para)
        placeholder = input("\n")
        print(Part3ContPara)
        DarthPlagueis()
        print("To cut Windu's hand, type 1.\n" + "To let him kill Palpatine, type 2.")
        Choice3Completed = False

        while Choice3Completed == False:
            Choice3 = input()

            if Choice3 == "1":
                Betrayal()
                print("You cut off Mace Windu's Hand!")
                Choice3Completed = True

            elif Choice3 == "2":
                Cantina()
                print("You let Master Windu kill Chancellor Palpatine!")
                Choice3Completed = True

            else:
                print("What you typed isn't an option! Try again.")

        # part 4 branch 1
        if Choice3 == "2":
            print(Part4Branch1Para)
            time.sleep(15)
            sa.stop_all()

        # part 4 branch 2
        elif Choice3 == "1":
            print(Part4Branch2Para)
            placeholder = input("\n")
            print(Part4Branch2Cont)
            Choice4Completed = False

            while Choice4Completed == False:
                Choice4 = input()

                if Choice4.casefold() == "1":
                    print("You have killed the younglings (lmao)!")
                    Choice4Completed = True

                elif Choice4.casefold() == "2":
                    print("You have spared the younglings!")
                    Choice4Completed = True

                else:
                    print("What you typed isn't an option! Try again.")

            # Part 5 Branch 1
            if Choice4 == "1":
                print(Part5Branch1Para)
                placeholder = input()
                print(Part5Branch1Cont)
                DontTryIt()
                print(Part5Branch1TryIt)
                Choice5Completed = False

                while Choice5Completed == False:
                    Choice5 = input()

                    if Choice5.casefold() == "1":
                        print(
                            "Uh Oh. Knowing full well Kenobi is the master of the High Ground, you tried it."
                        )
                        Choice5Completed = True

                    elif Choice5.casefold() == "2":
                        print("You did not try it, and instead retreated.")
                        Choice5Completed = True

                    else:
                        print("What you typed isn't an option! Try Again.")

                # Part 6 Branch 1
                if Choice5 == "1":
                    print(Part6Branch1Para)
                    Choice6Completed = False

                    while Choice6Completed == False:
                        Choice6 = input()

                        if Choice6.casefold() == "1":
                            print(IHateYou)
                            Immolation()
                            Choice6Completed = True

                        elif Choice6.casefold() == "2":
                            print(
                                "You stayed silent. Obi Wan watches in sadness as you get engulfed in flames."
                            )
                            Choice6Completed = True

                        else:
                            print("What you typed isn't an option! Try Again.")

                    # Part 7 Branch 1
                    if Choice6 == "1":
                        print(TragicHeroEnding)
                        Deeds()
                        time.sleep(15)
                        sa.stop_all()

                    # Part 7 Branch 2
                    if Choice6 == "2":
                        print(TragicHeroEnding)
                        Deeds()
                        time.sleep(15)
                        sa.stop_all()

                # Part 6 Branch 2
                if Choice5 == 0:
                    Deeds()
                    print(Part6Branch2Para)
                    Choice6Completed = False

                    while Choice6Completed == False:
                        Choice6 = input()

                        if Choice6.casefold() == "1":
                            print("You mercilessly killed Palpatine in his sleep.")
                            Choice6Completed = True

                        elif Choice6.casefold() == "2":
                            print("You stayed as Palpatine's apprentice!")
                            Choice6Completed = True

                        else:
                            print("What you typed isn't an option! Try Again.")

                    # Part 7 Branch 3
                    if Choice6 == "1":
                        ImpMarch()
                        print(JarJarEnding)
                        sa.stop_all()

                    # Part 7 Branch 4
                    elif Choice6 == "2":
                        print(OverPoweredEnding)
                        sa.stop_all()

            # Part 5 Branch 2
            elif Choice4 == "2":
                ImpMarch()
                print(Part5Branch2Para)
                time.sleep(5)
                sa.stop_all()


# Part 2 Branch 2
elif Choice1 == "2":
    print(Part2Branch2Para)
    sa.stop_all()
