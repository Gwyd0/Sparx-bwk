from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import json

FILE_NAME = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
CODES = []


class bcolors:
    # stolen from blender build script lmaoo
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class tags:
    error = bcolors.FAIL + "[ERROR] " + bcolors.ENDC
    main = bcolors.HEADER + "[MAIN] " + bcolors.ENDC
    log = "[LOG] "
    settings = "[SETTINGS] "


class info:
    USERNAME = ""
    PASSWORD = ""
    PATH = 'chromedriver.exe'  # path to chromedriver
    VERSION = '1.4 - Chrome - Win64'

    lastmsg = ""
    isopen = True
    autocontinue = False
    autobwk = False


def log(message):
    if info.lastmsg == message or len(message) < 34:
        return
    else:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S ", t)
        f = open("Logs/Log_{0}.txt".format(FILE_NAME), "a")
        f.write("{0} {1} \n".format(str(current_time), str(message)))
        f.close()
        print(current_time + message)
        info.lastmsg = message
        return


def savesettings():
    info.USERNAME = input(tags.log + "Please enter your sparx username: ")
    info.PASSWORD = input(tags.log + "Please enter your sparx password: ")
    INPUT1 = input(tags.log + "Do You want Autocontinue On? (skips games): ").casefold()
    INPUT2 = input(tags.log + "Do You want Autobwk On? (Does Bookwork CODES may fail): ").casefold()
    INPUT3 = input(tags.log + "Save Settings?: ").casefold()

    if INPUT1 == "true" or INPUT1 == "yes":
        info.autocontinue = True
        print(tags.log + "autocontinue enabled")
    if INPUT2 == "true" or INPUT2 == "yes":
        info.autobwk = True
        print(tags.log + "autobwk enabled")
    if INPUT3 == "true" or INPUT3 == "yes":
        print(tags.log + "saving settings. This may take some time")

        data = {'settings': [
            {'USERNAME': info.USERNAME, 'PASSWORD': info.PASSWORD, 'acon': info.autocontinue, 'abwk': info.autobwk}]}
        with open('Logs/settings.json', 'w') as outfile:
            json.dump(data, outfile)
        return
    else:
        print(tags.error + "Invalid argument")
        info.isopen = False
        return


def loadsettings():
    try:
        with open('Logs/settings.json') as json_file:
            data = json.load(json_file)
            print(tags.log + "Loading settings. This may take some time")
            info.USERNAME = data['settings'][0]['USERNAME']
            info.PASSWORD = data['settings'][0]['PASSWORD']
            info.autocontinue = data['settings'][0]['acon']
            info.autobwk = data['settings'][0]['abwk']
            return True
    except:
        return False


def makelogfile():
    try:
        f = open("Logs/Log_{0}.txt".format(FILE_NAME), "a")
        f.write(
            "[SPARX BWK LOGS]\n[START TIME] {0}\n--- [SETTINGS] --- \n[USER] {1}\n[PASSWORD] {2}\n["
            "AUTOCONTINUE] {3}\n[AUTOBWC] {4}\n[VERSION] {5}\n--- [WORK LOGS] --- \n".format(
                FILE_NAME, info.USERNAME, info.PASSWORD, str(info.autocontinue), str(info.autobwk), info.VERSION))
        f.close()
        log(tags.log + "Writing New Log")
        log(tags.log + "New Log Made [NAME] " + FILE_NAME)
        return
    except:
        log(tags.error + "FAILED TO WRITE LOG")
        return


def start():
    print(bcolors.OKBLUE + "By Gwyd0  VERSION." + info.VERSION + bcolors.ENDC)
    if not loadsettings():  # if loadsettings returns false then savesettings for next time.
        savesettings()

    makelogfile()
    log(tags.main + "If Chrome fails to open. Install the newest version of Chromedriver.")
    DRIVER = webdriver.Chrome(info.PATH)
    DRIVER.get(
        "https://westexe.sparxmaths.uk")

    USERNAME_ELEMENT = DRIVER.find_element(By.ID, "username")
    PASSWORD_ELEMENT = DRIVER.find_element(By.ID, "password")

    USERNAME_ELEMENT.send_keys(info.USERNAME)
    PASSWORD_ELEMENT.send_keys(info.PASSWORD)
    PASSWORD_ELEMENT.send_keys(Keys.RETURN)

    log(tags.main + "Chrome Version: " + str(DRIVER.capabilities['browserVersion']))
    print(bcolors.OKBLUE + "------------------ BOOKWORK CODES ------------------" + bcolors.ENDC)
    try:
        mainloop(DRIVER)
    except:
        print(bcolors.FAIL + "------------------ CHROME CLOSED ------------------" + bcolors.ENDC)
        info.isopen = False
        input(tags.error + "Exit to continue.")
        exit()


def mainloop(driver):
    while info.isopen:
        if "Sparx" in driver.title:
            try:
                BWK = driver.find_element(By.CLASS_NAME, 'bookwork-code')
                try:
                    kp = driver.find_element(By.CLASS_NAME, 'number-input')

                    if kp.get_attribute("value") != "":
                        log("[BWK] " + BWK.text + " [ANSWER] " + kp.get_attribute("value"))
                except:
                    d = 9
                try:
                    sl = driver.find_element(By.CLASS_NAME, 'selected')

                    if sl.text != "" and not "answer" in sl.text:
                        log("[BWK] " + BWK.text + " [ANSWER] " + sl.text)
                except:
                    if info.autocontinue:
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
