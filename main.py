import pyautogui as pt
from time import sleep

# Dict of keys and their corresponding actions (i.e. pressing "w" moves the character forward, pressing "a" makes the character attack)
# Make sure these match the keybinds in the game
actions = {"walkForward": "w", "walkBackward": "s", "attacking": "a", "mine": "m"}


def navToImage(image, clicks, off_x=0, off_y=0):
    pos = pt.locateCenterOnScreen(image, confidence=0.7)

    if pos is None:
        print(f"Could not find {image}")
        return False
    
    pt.moveTo(pos[0] + off_x, pos[1] + off_y, duration=0.1)
    pt.click(clicks=clicks, interval=0.25)
    return True

def moveCharacter(key, duration, action="walking"):
    pt.keyDown(key)

    if action == "walking":
        print("walking")
        sleep(duration)
    elif action == "attacking":
        print("attacking")
        pt.keyDown(actions["attacking"])
        sleep(duration)
        pt.keyUp(actions["attacking"])
    
    pt.keyUp(key)

def locateLava():
    pos = pt.locateCenterOnScreen("lava.png", confidence=0.35)

    if pos is None:
        print("Could not find lava")
        return False

    pt.keyDown(actions["walkBackward"])
    sleep(2)
    pt.keyUp(actions["walkBackward"])
    return pos


def main():
    sleep(5)
    navToImage("start.png", 1)

    while True:
        if locateLava():
            moveCharacter(actions["walkBackward"], 2)
            break

        moveCharacter(actions["walkForward"], 2)
        moveCharacter(actions["mine"], 2)


if __name__ == "__main__":
    main()
