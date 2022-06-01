# Example LED program.
# Plug in a single colored LED into port 1, a tri colored LED into tri-color
# port 2, a motor into motor port 1, a sound sensor in port 4, and
# a distance sensor into port 1.
# Place the distance sensor so it will not detect anything within 80cm of itself.
# To exit out of the program, move your hand in front of the distance sensor.
from BirdBrainLegacy import Hummingbird
from time import sleep

def main() -> int:
    humm = Hummingbird()
    while True:
        # Get distance from another object
        distance = humm.get_distance(1)
        
        if distance <= 20:
            wackTheHuman(humm)
        else:
            stopWackingTheHuman(humm)
            
    humm.close()
    return 0
    

def wackTheHuman(humm: Hummingbird) -> None:
    humm.set_tricolor_led(1, '#FF0000')
    humm.set_vibration_motor(1, 255)
    humm.set_servo(1, 90)
    sleep(1)
    humm.set_servo(1, 0)
    sleep(1)
    return

def stopWackingTheHuman(humm: Hummingbird) -> None:
    humm.set_tricolor_led(1, '#00FF00')
    humm.set_vibration_motor(1, 0)
    
if __name__ == "__main__":
    main()
