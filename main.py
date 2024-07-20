import qrcode
import pyfiglet
import time

ascii_Name = pyfiglet.Figlet(font='standard')
ascii_txt = ascii_Name.renderText("QR CODE GENERATOR")

print(ascii_txt)
print("(1): Create a qrcode")
print("(2): Exit...")
USER_MENU = int(input("Your selection: "))
exit = "Exit..."

def delay(exit, delay = 0.2):
    for i in exit:
        print(i, end = '', flush = True)
        time.sleep(delay)

while True:
    match USER_MENU:
        case 1:
            USER_URL = input("\nYour URL: ")
            USER_NAME_FILE = input("\nName of your Image: ")
        case 2:
            delay(exit)
            break
        case _:
            print("Select a valid option")

    if isinstance(USER_URL, str):
        img = qrcode.make(USER_URL)
        type(img)
        img.save(f"{USER_NAME_FILE}.png")
        print(f"\nYour file was saved as: {USER_NAME_FILE}")
        break
