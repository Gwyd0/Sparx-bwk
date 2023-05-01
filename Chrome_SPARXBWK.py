import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import json


FILE_NAME = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

class info:
    USERNAME = ""
    PASSWORD = ""
    PATH = 'chromedriver.exe'  # path to chromedriver
    VERSION = '1.3 - Gecko'

    lastMsg = ""
    isOpen = True
    AutoContinue = False
    AutoBWK = False
    OnLogin = False


def log(message): #writes to txt
    if info.lastMsg == message or len(message) < 34:
        return
    else:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S ", t)
        try:
            f = open("Logs/Log_{0}.txt".format(FILE_NAME), "a")
            f.write("{0} {1} \n".format(str(current_time), str(message)))
            f.close()
        except:
            log("[ERROR] 3 - Failed to log")

        print(current_time + message)
        info.lastMsg = message
        return


def saveSettings():
    info.USERNAME = input("[SETTINGS] Please enter your sparx username: ")
    info.PASSWORD = input("[SETTINGS] Please enter your sparx password: ")
    INPUT1 = input("[SETTINGS] Do You want Autocontinue On? (skips games): ").casefold()
    INPUT2 = input("[SETTINGS] Do You want Autobwk On? (Does Bookwork CODES may fail): ").casefold()
    INPUT3 = input("[SETTINGS] Save Settings?: ").casefold()

    if INPUT1 == "true" or INPUT1 == "yes":
        info.AutoContinue = True
        print("[SETTINGS] autocontinue enabled")
    if INPUT2 == "true" or INPUT2 == "yes":
        info.AutoBWK = True
        print("[SETTINGS] autobwk enabled")
    if INPUT3 == "true" or INPUT3 == "yes":
        print("[SETTINGS] saving settings. This may take some time")

        data = {'settings': [
            {'USERNAME': info.USERNAME, 'PASSWORD': info.PASSWORD, 'acon': info.AutoContinue, 'abwk': info.AutoBWK}]}
        with open('../../Desktop/Sparx-bwk-main - Copy/Sparx-bwk-main/Logs/settings.json', 'w') as outfile:
            json.dump(data, outfile)
        return
    else:
        print("[Error] Invalid argument")
        exit()


def loadSettings():
    try:
        with open('../../Desktop/Sparx-bwk-main - Copy/Sparx-bwk-main/Logs/settings.json') as json_file:
            data = json.load(json_file)
            print("[SETTINGS] Loading settings. This may take some time")
            info.USERNAME = data['settings'][0]['USERNAME']
            info.PASSWORD = data['settings'][0]['PASSWORD']
            info.AutoContinue = data['settings'][0]['acon']
            info.AutoBWK = data['settings'][0]['abwk']
            return True
    except:
        return False


def makeLogFile():
    try:

        f = open("Logs/Log_{0}.txt".format(FILE_NAME), "a")
        f.write(
            "[SPARX BWK LOGS]\n[START TIME] {0}\n--- [SETTINGS] --- \n[USER] {1}\n[PASSWORD] {2}\n["
            "AUTOCONTINUE] {3}\n[AUTOBWC] {4}\n[VERSION] {5}\n--- [WORK LOGS] --- \n".format(
                FILE_NAME, info.USERNAME, info.PASSWORD, str(info.AutoContinue), str(info.AutoBWK), info.VERSION))
        f.close()
        log("[LOG] Writing New Log")
        log("[LOG] New Log Made [NAME] " + FILE_NAME)
        return
    except:
        log("[ERROR] 2 - FAILED TO WRITE LOG")
        return


def start():
    print("By Gwyd0  VERSION." + info.VERSION)
    if not loadSettings():  # if loadsettings returns false then savesettings for next time.
        saveSettings()

    makeLogFile()

    DRIVER = webdriver.Chrome(info.PATH)

    DRIVER.get(
        "https://www.sparxmaths.uk/student")

    while not info.OnLogin:
        try:
            USERNAME_ELEMENT = DRIVER.find_element(By.ID, "username")
            PASSWORD_ELEMENT = DRIVER.find_element(By.ID, "password")

            USERNAME_ELEMENT.send_keys(info.USERNAME)
            PASSWORD_ELEMENT.send_keys(info.PASSWORD)
            PASSWORD_ELEMENT.send_keys(Keys.RETURN)

            info.OnLogin = True

        except:
            d = 1

    log("[MAIN] Chrome Version: " + str(DRIVER.capabilities['browserVersion']) + "\n[MAIN] If Chrome fails to open. install the newest version of geckodriver.\n------------------ BOOKWORK CODES ------------------")

    try:
        mainloop(DRIVER)
    except:
        log("[MAIN] Chrome Closed. Exiting")
        info.isOpen = False
        exit()


def mainloop(driver):
    while info.isOpen:
        if "Sparx" in driver.title:
            try:
                BWK = driver.find_element(By.CLASS_NAME, 'bookwork-code')
                try:
                    kp = driver.find_element(By.CLASS_NAME, 'number-input')

                    if kp.get_attribute("value") != "":
                        log("[BWK] " + BWK.text + " [ANSWER] " + kp.get_attribute("value").strip())
                except:
                    d = 9
                try:
                    sl = driver.find_element(By.CLASS_NAME, 'selected')

                    if sl.text != "" and not "answer" in sl.text and not sl.text.endswith("."):
                        log("[BWK] " + BWK.text + " [ANSWER] " + sl.text)
                except:
                    if info.AutoContinue:
                        a = driver.find_element(By.CLASS_NAME, "button-text")
                        b = driver.find_element(By.CLASS_NAME, "button-text")
                        if a.text == "Continue" or a.text == "Second chance":
                            a.click()
                        elif b.text == "Continue":
                            b.click()
            except:
                d = 1

if __name__ == '__main__':
    start()

