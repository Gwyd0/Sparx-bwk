from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import json

File_Name = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
codes = []


class info:
    un = ""
    pw = ""
    PATH = 'chromedriver.exe'
    v = '1.2'

    lastmsg = ""

    loggedin = True
    isopen = True

    autocontinue = False
    autobwk = False
    isaved = False


def log(l):
    if info.lastmsg == l:
        return
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    try:
        f = open("logs/Log_{0}.txt".format(File_Name), "a")
        f.write(str(current_time) + " " + l + "\n")
        f.close()
    except:
        log("[ERROR] 3 - Failed to log")

    print(current_time + " " + l)
    info.lastmsg = l
    codes.append(current_time + " " + l)


def savesettings():
    data = {'settings': [{'un': info.un, 'pw': info.pw, 'acon': info.autocontinue, 'abwk': info.autobwk}]}
    with open('Logs/settings.json', 'w') as outfile:
        json.dump(data, outfile)


def loadsettings():
    try:
        with open('Logs/settings.json') as json_file:
            data = json.load(json_file)
            info.isaved = True

            info.un = data['settings'][0]['un']
            info.pw = data['settings'][0]['pw']
            info.autocontinue = data['settings'][0]['acon']
            info.autobwk = data['settings'][0]['abwk']

    except:
        info.isaved = False


def makelogfile():
    try:
        f = open("logs/Log_{0}.txt".format(File_Name), "a")
        f.write("[SPARX BWK LOGS]\n")
        f.write("[START TIME] " + File_Name + "\n")
        f.write("[Logged In] " + str(info.loggedin) + "\n")
        f.write("--- [SETTINGS] --- \n")
        f.write("[USER] " + info.un + "\n")
        f.write("[PASSWORD] " + info.pw + "\n")
        f.write("[AUTOCONTINUE] " + str(info.autocontinue) + "\n")
        f.write("[AUTOBWC] " + str(info.autobwk) + "\n")
        f.write("[IS-SAVED] " + str(info.isaved) + "\n")
        f.write("[VERSION] " + info.v + "\n")
        f.write("--- [WORK LOGS] --- \n")
        f.close()
        log("[LOG] Writing New Log")
        log("[LOG] New Log Made [NAME] " + File_Name)
    except:
        log("[ERROR] 2 - FAILED TO WRITE LOG")
        exit()


def start():
    print(
        " ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄       ▄▄▄▄▄▄▄▄▄▄   ▄         ▄  ▄    ▄  \n"
        "▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌     ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░▌  ▐░▌ \n"
        "▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▐░▌   ▐░▌      ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌ ▐░▌  \n"
        "▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌  ▐░▌ ▐░▌       ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌   \n"
        "▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌   ▐░▐░▌        ▐░█▄▄▄▄▄▄▄█░▌▐░▌   ▄   ▐░▌▐░▌░▌    \n"
        "▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌    ▐░▌         ▐░░░░░░░░░░▌ ▐░▌  ▐░▌  ▐░▌▐░░▌     \n"
        " ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀    ▐░▌░▌        ▐░█▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌░▌ ▐░▌▐░▌░▌    \n"
        "          ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌    ▐░▌ ▐░▌       ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌▐░▌   \n"
        " ▄▄▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌       ▐░▌▐░▌      ▐░▌  ▐░▌   ▐░▌      ▐░█▄▄▄▄▄▄▄█░▌▐░▌░▌   ▐░▐░▌▐░▌ ▐░▌  \n"
        "▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌     ▐░░░░░░░░░░▌ ▐░░▌     ▐░░▌▐░▌  ▐░▌ \n"
        " ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀         ▀  ▀         ▀  ▀       ▀       ▀▀▀▀▀▀▀▀▀▀   ▀▀       ▀▀  ▀    ▀  \n"
    )
    print("By 7xzb  v." + info.v)
    loadsettings()

    if not info.isaved:
        info.un = input("[SETTINGS] Please enter your sparx username: ")
        info.pw = input("[SETTINGS] Please enter your sparx password: ")
        text1 = input("[SETTINGS] Do You want Autocontinue On? (skips games): ").casefold()
        text2 = input("[SETTINGS] Do You want Autobwk On? (Does Bookwork codes may fail): ").casefold()
        text3 = input("[SETTINGS] Save Settings?: ").casefold()

        makelogfile()

        if text1 == "true" or text1 == "yes":
            info.autocontinue = True
            log("[SETTINGS] autocontinue enabled")
        if text2 == "true" or text2 == "yes":
            info.autobwk = True
            log("[SETTINGS] autobwk enabled")
        if text3 == "true" or text3 == "yes":
            log("[SETTINGS] saving settings. This may take some time")
            savesettings()
    else:
        makelogfile()
        log("[SETTINGS] Loading settings. This may take some time")

    driver = webdriver.Chrome(info.PATH)
    driver.get("https://auth.sparxmaths.uk/oauth2/auth?client_id=sparx-maths-sw&hd=ad6ebaa5-6e59-4e31-9840"
               "-d14daad3bf03&redirect_uri=https%3A%2F%2Fstudentapi.api.sparxmaths.uk%2Foauth%2Fcallback"
               "&response_type=code&scope=openid+profile+email&state=-Gf6O5LrRF06ewfflb"
               "-6BwO7VgGjudj_LRkJeMZlnumzrnKLvu9ERDZdiBsIJvXKwOs6N6f39bssaU0HoaVsjZVdQ1S8KBvFxCMrnBBoCvQ7hWic_okVhmNeNBJfHhIzDPdQXGP9i0q-g4JzQxJsaucIW2Q22niy9t2r-T2BT9qVuwkujpGu9S203yvO80kpD5Rz0AM06qyGe5eDTShAXtbELago3LG_DFesTEHYFV-gRXjGv--lAERlN8gInjhGjmE%3D")

    log("[MAIN] If chrome fails to open. install the newest version of chromedriver.")

    un_ui = driver.find_element_by_id("username")
    pd_ui = driver.find_element_by_id("password")

    un_ui.send_keys(info.un)
    pd_ui.send_keys(info.pw)
    pd_ui.send_keys(Keys.RETURN)

    log("[MAIN] Chrome Version: " + str(driver.capabilities['browserVersion']))
    try:
        mainloop(driver)
    except:
        info.isopen = False
        log("[MAIN] Chrome Closed")

        textrun = input("[MAIN] RESTART?: ").casefold()

        if textrun == "true" or textrun == "yes":
            log("[MAIN] RESTARTING CHROME")
            info.isopen = True
            start()
        else:
            driver.quit()
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
