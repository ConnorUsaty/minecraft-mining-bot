import pyautogui as pt
from time import sleep

# Dict of keys and their corresponding actions (i.e. pressing "w" moves the character forward, pressing "a" makes the character attack)
# Make sure these match the keybinds in the game
actions = {"walkForward": "w", "walkBackward": "s", "attacking": "a", "turnLeft": "l"}


def readyToStart():
    try:
        pos = pt.locateCenterOnScreen('images/backToGame.png', confidence=0.6)
    except:
        return False
    
    pt.moveTo(pos[0], pos[1], duration=0.2)
    pt.click(clicks=1, interval=0.25)
    return True


def moveCharacter(key, duration, action="walking"):
    pt.keyDown(key)

    if action == "walking":
        sleep(duration)
    elif action == "attacking":
        pt.keyDown(actions["attacking"])
        sleep(duration)
        pt.keyUp(actions["attacking"])
    
    pt.keyUp(key)


def lavaFound():
    try:
        pt.locateCenterOnScreen("images/lava.png", confidence=0.4)
    except:
        return False
    
    return True


def main():
    # Wait for the game to load -> continously check for the "back to game" button
    while not readyToStart():
        sleep(1)

    # Track the number of consecutive left turns
    consecLeftTurns = 0

    # Main loop -> walk forward and mine until lava is found -> walk backwards and turn left -> continue mining
    while True:
        
        # If lava is found -> walk backwards and turn left -> then continue mining
        if lavaFound():
            moveCharacter(actions["walkBackward"], 2)
            moveCharacter(actions["turnLeft"], 1)
            consecLeftTurns += 1
            # Instead of turning left twice (180 degrees), and going down a path we already mined, we turn right so we can mine a new path
            if consecLeftTurns == 2:
                moveCharacter(actions["turnLeft"], 1)

        consecLeftTurns = 0
        moveCharacter(actions["walkForward"], 1, "attacking") # Walks forward and attacks (mines) for 2 seconds


if __name__ == "__main__":
    main()
