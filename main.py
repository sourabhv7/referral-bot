#   Creted By Sourabh Verma (geekerbuddy.cf)
#   github.com/sourabhv7

import pyautogui
import string
import random
import time
#x=783, y=681
url = 'https://codedamn.com/referred-by/sonu7'   #paste your link here
def ran_string(N):
    
    

    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k = N))
    return res
def run():
    pyautogui.hotkey('ctrl', 'shift', 'p')
    time.sleep(1)
    pyautogui.typewrite(url)
    pyautogui.press('enter')
    pyautogui.sleep(4)
    pyautogui.click(x=783, y=681, clicks=1,interval=0.0,button='left')
    username = ran_string(6)
    pyautogui.typewrite(username)
    pyautogui.press('enter')
    email = username+ "@gmail.com"
    pyautogui.typewrite(email)
    pyautogui.press('enter')
    password = ran_string(10)
    pyautogui.typewrite(password)
    pyautogui.press('enter')
    time.sleep(1.5)


if __name__ == '__main__':
    time.sleep(5)
    n=2
    while n > 0:
        run()
        print(n)
        n -= 1
        
    


