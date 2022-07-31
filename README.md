# Sparx Cheats
**Sparx-Bookwork-Code** is a project ive been working on for about a year (mostly as a hobby and because im lazy).

Its a web scraper to log Bookwork codes for Sparx and auto completes Bookwork checks (explained [here](https://support.sparx.co.uk/en/knowledge/what-is-a-bookwork-check-and-why-are-they-used-in-sparx)). It uses chromedriver (google chrome) to grab the values of answers and codes. I use python as its my main launguage and is quite easy to understand.

As i have stoped using sparx, its no use to me anymore so having it here may help anybody who wants to automate their Sparx math homework.

## Basic features
* auto fills in password + username
* logs codes for every question
* auto does bookwork checks.
* creates a full backup log as a .txt in /logs

## Setup
This only works for **chrome** so make sure you have **chrome installed**.
### Windows
Simply, download the code and run the .exe
You may have to update Chromedriver as explained below.

## Bugs
* Chromedriver needs updating about twice every month, you can download it [here](https://chromedriver.chromium.org/downloads), Download the same version
as your browser. then place chromedriver.exe in the same directory as the .exe or .py
* Sometimes Auto Bookwork checks may not work (due to how fractions are displayed). 
* Make Sure that the .exe or .py file are in the same directory as the **Logs** file.
## Why so many Try and excepts?
If you can be bothered to read my code. You might notice the amount of try: and excepts there are, this is because of **Selenium Webdirver**.

For some reason, Selenium will crash if it can't find an element. This means that to avoid crashing i have to use try-excepts, like this:
``` python
try:
  kp = driver.find_element_by_class_name('number-input')
  if kp.get_attribute("value") != "":
    log("[BWK] " + BWK.text + " [ANSWER] " + kp.get_attribute("value"))
except:
```
and.. as i check for multiple elements, the result is a lot of try-excepts.
