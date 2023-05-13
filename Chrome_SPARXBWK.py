import selenium

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# for chromedriver
import requests
import wget
import zipfile
import os

FILE_NAME = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")


class info:
    USERNAME = ""
    PASSWORD = ""
    PATH = 'chromedriver.exe'  # path to chromedriver
    VERSION = '1.4.5 - Chrome'

    isOpen = True
    AutoContinue = False
    AutoBWK = False
    OnLogin = False

    tmp_messages = ["placeholder","placeholder","placeholder"]


def log(message):  # writes to txt
    if info.tmp_messages[-1] == message or info.tmp_messages[-2] == message or info.tmp_messages[-3] == message:  # this is quicker than going through the entire thing.
        return
    elif message.__contains__("BWK") and len(message) < 35:
        return
    else:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S ", t)
        try:
            f = open("Logs/Log_{0}.txt".format(FILE_NAME), "a")
            f.write("{0} {1} \n".format(str(current_time), str(message)))
            f.close()
        except:
            d = 12 # placeholder

        print(current_time + message)
        info.tmp_messages.append(message)
        return


def saveSettings():
    info.USERNAME = input("[SETTINGS] Please enter your sparx username: ")
    info.PASSWORD = input("[SETTINGS] Please enter your sparx password: ")

    INPUT1 = input("[SETTINGS] Do You want Autocontinue On? (skips games): ").casefold()
    INPUT2 = input("[SETTINGS] Do You want Autobwk On? (This is disabled cos of fractions. Blame sparx.): ").casefold()
    INPUT3 = input("[SETTINGS] Save Settings?: ").casefold()

    if INPUT1 == "true" or INPUT1 == "yes" or INPUT1 == "y":
        info.AutoContinue = True
    if INPUT2 == "true" or INPUT2 == "yes" or INPUT2 == "y":
        info.AutoBWK = True
    if INPUT3 == "true" or INPUT3 == "yes" or INPUT3 == "y":
        print("[SETTINGS] Saving settings. This may take some time")

        data = {'settings': [
            {'USERNAME': info.USERNAME, 'PASSWORD': info.PASSWORD, 'acon': info.AutoContinue, 'abwk': info.AutoBWK}]}
        try:
            with open('Logs/settings.json', 'w') as outfile:
                json.dump(data, outfile)
            return

        except FileNotFoundError:
            print(
                "--------\n[Error] Failed writing settings. Make sure the there is a folder called 'Logs' in the same "
                "folder"
                "as the .exe")
            input()
            exit()
    else:
        print("[Error] Invalid argument use 'y' or 'Yes'\nPress any button to exit.")
        input()
        exit()


def loadSettings():
    try:
        with open('Logs/settings.json') as json_file:
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


def downloadChromedriver():  # Downloads the correct version of chromedriver
    print("[SETUP] Installing latest chromedriver version, This may take a some time.")
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    download_url = "https://chromedriver.storage.googleapis.com/" + version_number + "/chromedriver_win32.zip"
    latest_driver_zip = wget.download(download_url, 'chromedriver.zip')

    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove(latest_driver_zip)


def start():
    print(
        "-------------------------------\nSPARXBWK\n-------------------------------\nBy Gwyd0  VERSION " + info.VERSION + "\n")
    if not loadSettings():  # if loadsettings returns false then savesettings for next time.
        saveSettings()
        downloadChromedriver()

    makeLogFile()

    options = Options()
    options.add_argument("start-maximized")
    DRIVER = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

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
    log("[MAIN] Chrome Version: " + str(DRIVER.capabilities[
                                            'browserVersion']) + "\n[MAIN] If Chrome fails to open. install the newest version of chromedriver.\n------------------ BOOKWORK CODES ------------------")

    try:
        mainloop(DRIVER)
    except:
        log("[MAIN] Chrome Closed. Exiting")
        info.isOpen = False
        input()
        exit()


def mainloop(driver):
    while info.isOpen:
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
                    if sl.text != "" and not sl.text.__contains__("Select") and not sl.text.endswith("."):
                        log("[BWK] " + BWK.text + " [ANSWER] " + sl.text.replace('\n', ''))
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
