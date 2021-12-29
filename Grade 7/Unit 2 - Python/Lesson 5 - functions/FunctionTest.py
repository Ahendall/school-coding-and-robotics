import time

def HelloThere(x):
    for y in range(x):
        print("Hello there")
        time.sleep(0.1)

def SeveralKenobi():
    print("""Several Keno- Wait, what?
    Several Kenobi?
    Nah I'm gone
    """)

def YourMove(x):
    for y in range(x):
        print("Your Move")
        time.sleep(0.1)

HelloThere(5)
time.sleep(0.5)
SeveralKenobi()
time.sleep(0.5)
YourMove(50)