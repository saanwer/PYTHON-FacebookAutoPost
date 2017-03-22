import argparse, os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pykeyboard import PyKeyboard
#Facebook Auto Login & Status Update
#Coded by | WarLord
#https://github.com/saanwer
def getID(url):
    pUrl = urlparse.urlparse(url)
    return urlparse.parse_qs(pUrl.query)['id'][0]

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("email", help="Facebook email")
    parser.add_argument("password", help="Facebook password")
    parser.add_argument("status", help="Facebook status")

    args = parser.parse_args()

    browser = webdriver.Firefox()
    browser.get("https://www.facebook.com/login.php")

    emailElement = browser.find_element_by_id("email")
    emailElement.send_keys(args.email)
    passElement = browser.find_element_by_id("pass")
    passElement.send_keys(args.password)
    passElement.submit()
    time.sleep(5)
    browser.get("https://m.facebook.com/")#Change it to m.facebook.com/yourfriend if you need to post on your friend's wall
    time.sleep(2)
    statusElement = browser.find_element_by_id("u_0_0")
    statusElement.send_keys(args.status)
    keyboard = PyKeyboard()
    keyboard.press_key(keyboard.tab_key)#Keyboard press 'TAB'
    keyboard.press_key(keyboard.enter_key)#Keyboard press 'ENTER'
    
    os.system('cls')#os.system('clear') if Linux
    print "[+] Auto login success!"
    browser.close()

if __name__ == "__main__":
    Main()
