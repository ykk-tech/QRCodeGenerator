# Import the QR Code Library and the Time Library.
import qrcode
import time

# Make the while loop infinitely run until isrunning set to false
isrunning = True

# Sleep function to save time.
def sleep1():
    time.sleep(1)

# My function
def mysignature():
    print("This script was made by @ykk-tech on github.")

# Introduction
while isrunning:
    print("Welcome to the QR Code Generator.")
    sleep1()

    # Asks the User for the Website
    data = input("Please enter your website (https://www.example.com) here: ").strip().lower()
    datagithub = "https://github.com/ykk-tech"
    sleep1()
    print("Okay! Generating your QR Code.")

    # Create the QR Code
    qr = qrcode.QRCode(
        version=8,  # Size of QR Code (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the Data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create the image from the QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Saves the QR Code
    sleep1()
    imagesaved = input("What would you like your image to be called: ")
    img.save(imagesaved + ".png")
    sleep1()
    print(f"QR Code generated and saved as '{imagesaved}.png'.")
    sleep1()
    rerunscript = input("Would you like to re-run the script? (yes / no): ").strip().lower()
    sleep1()
    if rerunscript == "yes":
        print("Okay! Directing you back to generate another QR Code.")
    if rerunscript == "no":
        askgithub = input("Okay! Would you like to view my github for other projects? (yes / no): ").strip().lower()
        if askgithub == "no":
            print("Okay. Exiting you out of the script.")
            sleep1()
            isrunning = False
        if askgithub == "yes":
            mysignature()
            qrcodegithub = input("Would you like a qr code made of my github? (yes / no): ").strip().lower()
            sleep1()
            if qrcodegithub == "yes":
                sleep1()
                print("Okay! Making your QR Code.")
                qr = qrcode.QRCode(
                    version=8,  # Size of QR Code (1-40)
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(datagithub)
                qr.make(fit=True)
                img_github = qr.make_image(fill_color="black", back_color="white")
                sleep1()
                img_github.save("MyGithub.png")
                print("Github Saved!")
                sleep1()
                isrunning = False
            elif qrcodegithub == "no":
                print("Okay! Exiting the script.")
                sleep1()
                isrunning = False
            else:
                print("Invalid answer! Exiting you out of the script.")
                sleep1()
                isrunning = False