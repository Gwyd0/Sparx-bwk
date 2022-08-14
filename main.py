from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import json

FILE_NAME = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
CODES = []

class info:
    USERNAME = ""
    PASSWORD = ""
    PATH = 'chromedriver.exe' # path to chromedriver
    VERSION = '1.2'

    lastmsg = ""
    isopen = True
    autocontinue = False
    autobwk = False


def log(message):
    if info.lastmsg == message:
        return
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    try:
        f = open("logs/Log_{0}.txt".format(FILE_NAME), "a")
        f.write("{0} {1} \n".format(str(current_time),message))
        f.close()
    except:
        log("[ERROR] 3 - Failed to log")

    print(current_time + " " + message)
    info.lastmsg = message


def savesettings():
    info.USERNAME = input("[SETTINGS] Please enter your sparx username: ")
    info.PASSWORD = input("[SETTINGS] Please enter your sparx password: ")
    text1 = input("[SETTINGS] Do You want Autocontinue On? (skips games): ").casefold()
    text2 = input("[SETTINGS] Do You want Autobwk On? (Does Bookwork CODES may fail): ").casefold()
    text3 = input("[SETTINGS] Save Settings?: ").casefold()

    if text1 == "true" or text1 == "yes":
        info.autocontinue = True
        print("[SETTINGS] autocontinue enabled")
    elif text2 == "true" or text2 == "yes":
        info.autobwk = True
        print("[SETTINGS] autobwk enabled")
    elif text3 == "true" or text3 == "yes":
        print("[SETTINGS] saving settings. This may take some time")
        
        data = {'settings': [{'USERNAME': info.USERNAME, 'PASSWORD': info.PASSWORD, 'acon': info.autocontinue, 'abwk': info.autobwk}]}
        with open('Logs/settings.json', 'w') as outfile:
            json.dump(data, outfile)
        return
    else:
        print("[Error] Invalid argument")
        exit


def loadsettings():
    try:
        with open('Logs/settings.json') as json_file:
            data = json.load(json_file)
            print("[SETTINGS] Loading settings. This may take some time")
            info.USERNAME = data['settings'][0]['USERNAME']
            info.PASSWORD = data['settings'][0]['PASSWORD']
            info.autocontinue = data['settings'][0]['acon']
            info.autobwk = data['settings'][0]['abwk']
            return True

    except:
        return False


def makelogfile():
    try:
        f = open("logs/Log_{0}.txt".format(FILE_NAME), "a")
        f.write("[SPARX BWK LOGS]\n[START TIME] {0}\n[Logged In] {1} \n--- [SETTINGS] --- \n[USER] {2}\n[PASSWORD] {3}\n[AUTOCONTINUE] {4}\n[AUTOBWC] {5}\n[IS-SAVED] {6}\n[VERSION] {7}\n--- [WORK LOGS] --- \n" .format(
            FILE_NAME,str(info.loggedin),info.USERNAME,info.PASSWORD,str(info.autocontinue),str(info.autobwk),str(info.isaved),info.VERSION))
        f.close()
        log("[LOG] Writing New Log")
        log("[LOG] New Log Made [NAME] " + FILE_NAME)
        return
    except:
        log("[ERROR] 2 - FAILED TO WRITE LOG")
        return


def start():
    print(" ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄       ▄▄▄▄▄▄▄▄▄▄   ▄         ▄  ▄    ▄  \n""▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌     ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░▌  ▐░▌ \n""▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▐░▌   ▐░▌      ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌ ▐░▌  \n""▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌  ▐░▌ ▐░▌       ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌   \n""▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌   ▐░▐░▌        ▐░█▄▄▄▄▄▄▄█░▌▐░▌   ▄   ▐░▌▐░▌░▌    \n""▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌    ▐░▌         ▐░░░░░░░░░░▌ ▐░▌  ▐░▌  ▐░▌▐░░▌     \n"" ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀    ▐░▌░▌        ▐░█▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌░▌ ▐░▌▐░▌░▌    \n""          ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌    ▐░▌ ▐░▌       ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌▐░▌   \n"" ▄▄▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌       ▐░▌▐░▌      ▐░▌  ▐░▌   ▐░▌      ▐░█▄▄▄▄▄▄▄█░▌▐░▌░▌   ▐░▐░▌▐░▌ ▐░▌  \n""▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌     ▐░░░░░░░░░░▌ ▐░░▌     ▐░░▌▐░▌  ▐░▌ \n"" ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀         ▀  ▀         ▀  ▀       ▀       ▀▀▀▀▀▀▀▀▀▀   ▀▀       ▀▀  ▀    ▀  \nBy Gwyd0  VERSION." + info.VERSION)
    
    if not loadsettings(): # if loadsettings returns false then savesettings for next time.
        savesettings()

    makelogfile()

    driver = webdriver.Chrome(info.PATH)
    driver.get("https://auth.sparxmaths.uk/oauth2/auth?client_id=sparx-maths-sw")

    USERNAME_ELEMENT = driver.find_element_by_id("username")
    PASSWORD_ELEMENT = driver.find_element_by_id("password")

    USERNAME_ELEMENT.send_keys(info.USERNAME)
    PASSWORD_ELEMENT.send_keys(info.PASSWORD)
    PASSWORD_ELEMENT.send_keys(Keys.RETURN)

    log("[MAIN] Chrome Version: " + str(driver.capabilities['browserVersion']))
    log("[MAIN] If chrome fails to open. install the newest version of chromedriver.")
    try:
        mainloop(driver)
    except:
        log("[MAIN] Chrome Closed. Exiting.")
        info.isopen = False
        exit()



def mainloop(driver):
    while info.isopen:
        if driver.find_element_by_class_name("location-title").text != "Homework":
            try:
                BWK = driver.find_element_by_xpath('//*[@id="top-bar"]/div/div[1]/span')
                try:
                    kp = driver.find_element_by_class_name('number-input')
                    if kp.get_attribute("value") != "":
                        log("[BWK] " + BWK.text + " [ANSWER] " + kp.get_attribute("value"))
                        #CODES.append(BWK.text + "/" + kp.get_attribute("value")) for auto checks
                except:
                    try:
                        sl = driver.find_element_by_class_name('selected')
                        if sl.text != "" and not "answer" in sl.text:
                            log("[BWK] " + BWK.text + " [ANSWER] " + sl.text)
                    except:
                        try:
                            if info.autocontinue:
                                a = driver.find_element_by_class_name('button-text')
                                if a.text == "Continue":
                                    a.click()
                                b = driver.find_element_by_class_name('alert-button')
                                if b.text == "Continue":
                                    a.click()
                        except:
                            d = 0
            except:
                d = 1


if __name__ == '__main__':
    start()
