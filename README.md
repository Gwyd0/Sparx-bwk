# Sparx-BWK
**Sparx-Bookwork-Code** is a project I've been working on for about a year (mostly as a hobby and because I'm lazy).


It's a web scraper to log Bookwork codes for Sparx and auto completes Bookwork checks (explained [here](https://support.sparx.co.uk/en/knowledge/what-is-a-bookwork-check-and-why-are-they-used-in-sparx)). It uses chrome driver (Google Chrome) to grab the values of answers and codes. I use python as it's my main language and is quite easy to understand.

As I have stopped using Sparx, it's no use to me any more, so having it here may help anybody who wants to automate their Sparx maths homework.

## Basic features
* Auto fills in password + username
* Logs codes for every question
* Auto does bookwork checks.
* Creates a full backup log as a .txt in /logs

## Setup
This only works for **chrome,** so make sure you have **chrome installed**.
### Windows
* Clone the repo and run the .exe
* Make Sure that the .exe or .py file are in the same directory as the **Logs** file, if not the .exe/.py should create one.
You may have to update Chrome driver, as explained below.

## Bugs
* Chrome driver needs updating about twice every month, you can download it [here](https://chromedriver.chromium.org/downloads), Download the same version
as your browser. Then place chromedriver.exe in the same directory as the .exe or .py
* Sometimes Auto bookwork checks may not work (due to how fractions are displayed). 
## Why so many try and excepts?
If you can be bothered to read my code. You might notice the amount of try: and excepts there are, this is because of **Selenium Webdriver**.

For some reason, Selenium will crash if it can't find an element. This means that to avoid crashing I have to use try-excepts, like this:
``` python
try:
  kp = driver.find_element_by_class_name('number-input')
  if kp.get_attribute("value") != "":
    log("[BWK] " + BWK.text + " [ANSWER] " + kp.get_attribute("value"))
except:
```
And... as I check for multiple elements, the result is a lot of try-excepts.
