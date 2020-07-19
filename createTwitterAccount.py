#! python3
# mouseNow.py - Displays the mouse cursor's current position
import pyautogui, time
print('Press Ctrl-C to quit.')

try:
    # Open Chrome and go to Gmail
    pyautogui.click(564, 1059)
    pyautogui.click(209, 52)
    pyautogui.typewrite(['backspace'])
    pyautogui.typewrite('accounts.google.com\n')
    time.sleep(5)

    pyautogui.click(829, 726)
    time.sleep(1)
    pyautogui.click(829, 781)
    time.sleep(1)
    # First Name
    pyautogui.click(714, 480)
    pyautogui.typewrite('Zilros')  # update with input from user
    # Last Name
    pyautogui.click(900, 480)
    pyautogui.typewrite('Sparklegem')  # update with input from user
    # Username
    pyautogui.click(746, 541)
    pyautogui.typewrite('zilros.sparklegem')  # update with input from user
    # Password
    pyautogui.click(681, 653)
    pyautogui.typewrite('How do you want to do this?')
    # Confirm Password
    pyautogui.click(864, 653)
    pyautogui.typewrite('How do you want to do this?')
    time.sleep(1)
    pyautogui.click(957, 775)
    """pyautogui.click(209, 52)
    pyautogui.typewrite(['backspace'])
    pyautogui.typewrite('twitter.com\n')
    time.sleep(5)

    # Start account sign up process
    pyautogui.click(1352, 126)
    pyautogui.click(744, 568)
    pyautogui.click(731, 409)
    pyautogui.typewrite('Aldros Sparklegem')  # update with input from user
    time.sleep(2)
    pyautogui.click(731, 511)
    pyautogui.typewrite('aldros.sparklegem@gmail.com')  # update with input from user
    pyautogui.click(717, 714)
    pyautogui.typewrite('December')
    pyautogui.click(977, 714)
    pyautogui.typewrite('23')
    pyautogui.click(1107, 714)
    pyautogui.typewrite('1992')
    pyautogui.click(952, 815)
    pyautogui.click(1213, 271)
    time.sleep(1)
    pyautogui.click(1219, 412)
    pyautogui.click(1213, 271)

    # need to add double check step here to continue
    time.sleep(1)
    pyautogui.click(952, 751)
    pyautogui.click(735, 427)

    # get 2FA code
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('v')
    pyautogui.keyUp('ctrlleft')
    pyautogui.click(1213, 271)
    pyautogui.click(721, 427)
    pyautogui.typewrite('How do you want to do this?')
    time.sleep(1)
    pyautogui.click(1213, 271)

    # profile pic (usually skip, can add functionality later)
    pyautogui.click(1183, 271)

    # add bio
    pyautogui.click(740, 443)
    pyautogui.typewrite("I'm a pretty cool dude!") # Add user input
    pyautogui.click(1213, 271)

    # Add interests etc. (Usually skip)
    pyautogui.click(950, 711)
    pyautogui.click(1183, 271)
    pyautogui.click(1213, 271)
    pyautogui.click(959, 759)
    """

    # COMPLETE

except KeyboardInterrupt:
    print('\nDone.')