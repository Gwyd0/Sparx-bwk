from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import requests
import time
import json

FILE_NAME = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
CODES = []


class info:
    USERNAME = ""
    PASSWORD = ""
    SCHOOL = ""
    PATH = 'chromedriver.exe'  # path to chromedriver
    VERSION = '1.3 - Chrome'

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
    info.USERNAME = input("[SETTINGS] Please enter your Sparx username: ")
    info.PASSWORD = input("[SETTINGS] Please enter your Sparx password: ")
    info.SCHOOL = input("[SETTINGS] Please enter your School Name (full name): ")
    INPUT1 = input("[SETTINGS] Do you want Auto Continue On? (skips games): ").casefold()
    INPUT2 = input("[SETTINGS] Do you want Auto Bwk On? (does Bookwork CODES, may fail): ").casefold()
    INPUT3 = input("[SETTINGS] Save Settings?: ").casefold()

    if INPUT1 == "true" or INPUT1 == "yes":
        info.autocontinue = True
        print("[SETTINGS] Auto Continue enabled")
    if INPUT2 == "true" or INPUT2 == "yes":
        info.autobwk = True
        print("[SETTINGS] Auto Bwk enabled")
    if INPUT3 == "true" or INPUT3 == "yes":
        print("[SETTINGS] Saving Settings. This may take some time.")

        data = {'settings': [
            {'USERNAME': info.USERNAME, 'PASSWORD': info.PASSWORD, 'SCHOOL': info.SCHOOL, 'acon': info.autocontinue, 'abwk': info.autobwk}]}
        with open('Logs/settings.json', 'w') as outfile:
            json.dump(data, outfile)
        return
    else:
        print("[Error] Invalid argument")
        exit()


def loadsettings():
    try:
        with open('Logs/settings.json') as json_file:
            data = json.load(json_file)
            print("[SETTINGS] Loading settings. This may take some time.")
            info.USERNAME = data['settings'][0]['USERNAME']
            info.PASSWORD = data['settings'][0]['PASSWORD']
            info.SCHOOL = data['settings'][0]['SCHOOL']
            info.autocontinue = data['settings'][0]['acon']
            info.autobwk = data['settings'][0]['abwk']
            return True
    except:
        return False


def makelogfile():
    try:
        f = open("Logs/Log_{0}.txt".format(FILE_NAME), "a")
        f.write(
            "[SPARX BWK LOGS]\n[START TIME] {0}\n--- [SETTINGS] --- \n[USER] {1}\n[PASSWORD] {2}\n[SCHOOL] {3}\n["
            "AUTOCONTINUE] {3}\n[AUTOBWC] {4}\n[VERSION] {5}\n--- [WORK LOGS] --- \n".format(
                FILE_NAME, info.USERNAME, info.PASSWORD, info.SCHOOL, str(info.autocontinue), str(info.autobwk), info.VERSION))
        f.close()
        log("[LOG] Writing New Log.")
        log("[LOG] New Log Made [NAME] " + FILE_NAME + ".")
        return
    except:
        log("[ERROR] 2 - FAILED TO WRITE LOG.")
        return

def get_auth_url():
    response = requests.get("https://schoolsearch.api.sparxmaths.uk/v1/search?query=" + info.SCHOOL.replace(" ", "%20"))
    response = response.json()["matches"]
    if len(response) == 0:
        return False
    else:
        return "https://auth.sparxmaths.uk/oauth2/auth?client_id=sparx-maths-sw&hd=" + response[0]["school"]["school_id"] + "&redirect_uri=https%3A%2F%2Fstudentapi.api.sparxmaths.uk%2Foauth%2Fcallback&response_type=code&scope=openid+profile+email&state=Fsb04bwAyXGRuvFksrtO-QqR5XU_rswZ2YI4jjAXyIjuKfs5GN1RzzFz40FYmyiuUksh2SoOVWeBYNk_1LZWy2FjPgJyKalJyAF-HiZhyhhLP3PNW2vx1jKAVLbFWl0eYNZ20jcUB83M687pYzcPxxuj0kyqyr3VdEfKui1LliaJHZFFd857NAX-PrDGbEOC4S-tug48z9PTmUZ2PA0VkF2Y0lNDbcNeZx8lh5c5dJMKfYNRiK3Zta07zgihjWUZzbs3mVObYD0%3D"

def start():
    print("By Gwyd0  VERSION." + info.VERSION)
    if not loadsettings():  # if loadsettings returns false then savesettings for next time.
        savesettings()

    makelogfile()
    log("[MAIN] If Chrome fails to open. Install the newest version of Chromedriver.")
    DRIVER = webdriver.Chrome(info.PATH)
    auth_url = get_auth_url()
    if auth_url == False:
        log("[ERROR] You have provided an Invalid School Name. Please ensure the name is typed correctly.")
        print("[ERROR] You have provided an Invalid School Name. Please ensure the name is typed correctly.")
        time.sleep(5)
        exit()
    DRIVER.get(auth_url)

    USERNAME_ELEMENT = DRIVER.find_element(By.ID, "username")
    PASSWORD_ELEMENT = DRIVER.find_element(By.ID, "password")

    USERNAME_ELEMENT.send_keys(info.USERNAME)
    PASSWORD_ELEMENT.send_keys(info.PASSWORD)
    PASSWORD_ELEMENT.send_keys(Keys.RETURN)

    log("[MAIN] Chrome Version: " + str(DRIVER.capabilities['browserVersion']))

    try:
        mainloop(DRIVER)
    except:
        log("[MAIN] Chrome Closed. Exiting.")
        info.isopen = False
        input("Exit to continue.")
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
