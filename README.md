# Sparx-BWK
**Sparx-Bookwork-Code** is a project I've been working on for about a year (mostly as a hobby and because I'm lazy).


It's a web scraper to log Bookwork codes for Sparx and auto completes Bookwork checks (explained [here](https://support.sparx.co.uk/docs/what-are-bookwork-checks)). It uses chrome driver (Google Chrome) to grab the values of answers and codes. I use python as it's my main language and is quite easy to understand.

As I have stopped using Sparx, it's no use to me any more, so having it here may help anybody who wants to automate their Sparx maths homework.

## Basic features
* Auto fills in password + username
* Logs codes for every question
* Auto does bookwork checks. (Currently reworking it)
* Creates a full backup log of every question as a .txt in /Logs

## Setup Step by Step
### Step 1: Install Chrome
This is mainly dedicated to chrome. Other web browsers are too much work to keep up to date, so make sure you have Chrome installed.
Once Chrome is installed, you need to figure out what version it is (Chromedriver is very picky about versions).

First, navigate to the three dots in the top right.
then go to
Settings > About Chrome (it's at the bottom) and look at the version.

Then go to [here](https://chromedriver.chromium.org/downloads) and download the version you have.

### Step 2: Download Repo
Next, click [here](https://github.com/Gwyd0/Sparx-bwk/archive/refs/heads/main.zip). This should download the rest of the files you need.
* First, right-click the file and click "Extract All"
Next, open the extracted file and open Sparx-bwk-main.
* Place the chromedriver file you downloaded in step 1 in the file; it should be in the same file as the.exe and readme.md.

### Step 3: Run the file.
![capture1](https://raw.githubusercontent.com/Gwyd0/Sparx-bwk/main/Images/Capture2.PNG?raw=True) <br>
Your folder should look something like that
Now run the.exe called "BWK-CHROME.
Windows may come up with this; just click "more info." Run anyway.

Type in the details, and you're done. Chrome should open, and your bookwork codes should be logged for you.
![capture1](https://raw.githubusercontent.com/Gwyd0/Sparx-bwk/main/Images/Capture1.PNG?raw=True) <br>

## Bugs
* Chrome driver needs updating about twice every month, you can download it [here](https://chromedriver.chromium.org/downloads), Download the same version
as your browser. Then place chromedriver.exe in the same directory as the .exe or .py
* Sometimes Auto bookwork checks may not work (due to how fractions are displayed). 
* Bug where window wont close without crashing (fixing this soon)
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
