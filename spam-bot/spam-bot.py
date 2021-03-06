import os, sys

# Restructure path to the script
sys.path.append(os.path.realpath('..'))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from os import system, name as osname
from alive_progress import alive_bar
import utils.login.discord_login as discord_login
from pickle import load
from time import sleep
import random
import time

def retrieve_credentials():
    try:
        frobj = open("../utils/login/credentials.dat", "rb")
        details = load(frobj)
        frobj.close()
        return details
    except:
        return None

def clearscreen():
    system('cls' if osname == 'nt' else 'clear')
    print("\n", "-"*25, "DISCORD SPAM BOT", "-"*25, "\n")

# Opening link and logging in
def login(link, email, passwd):
    # Initialising/Installing Chromedriver
    global driver, flag, templink
    if (flag == False):
        driver = webdriver.Chrome(ChromeDriverManager().install(), service_log_path = None)
    if (link != templink):
        print("\nLoading Discord...\n")
        driver.get(link)
        templink = link
    if (flag == False):
        clearscreen()
        myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'email')))
        print("\nLogging in...")
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('password').send_keys(passwd)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)
        sleep(5)
        print("\nLogged in successfully")
        flag = True
    sleep(1)
    clearscreen()

# Retrieve data from the text file
def retrieve_messages():
    with open("messages/messages.txt") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]
    print(f'\n******* Text File loaded with {len(data)} messages *******')  
    return data

# Create spam logs
def create_logs(logs):
    localtime = time.localtime()
    timeStamp = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
    
    with open(f'logs/{timeStamp}.txt', 'w') as file:
        for log in logs:
            file.write(log)
            file.write('\n')

# Starting spam
def spam(n, messages, intervals):
    logs = []
    system('cls' if osname == 'nt' else 'clear')
    with alive_bar(n, title='Sending Messages', bar='classic2', spinner='classic') as bar:
        for i in range(n):
            localtime = time.localtime()
            timeStamp = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
            
            randomWrd = random.choice(messages)
            randomTime = random.choice(intervals)
            
            actions = ActionChains(driver)
            actions.send_keys(randomWrd)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            bar()
            sleep(randomTime)
            
            logs.append(f'{str(i).zfill(3)} - {randomTime}s - {timeStamp} - {randomWrd}')
    print("\nAll Messages Sent")
    # Creaete logs according to the time stamp
    create_logs(logs)

# Menu
def main():
    global flag
    flag = False
    intervals = []
    time_interval = ""

    details = retrieve_credentials()
    messages = retrieve_messages()
    
    if (details != None):
        email, passwd = details
    else:
        discord_login.store()
        main()

    try:
        while True:
            clearscreen()
            link = input("\nEnter link to channel: ")
            num_of_msg = int(input("Enter number of messages: "))

            while True:
                time_interval = input("Enter time interval between messages (in seconds): ")
                if (time_interval == "q"):
                    break
                intervals.append(int(time_interval))

            login(link, email, passwd)
            spam(num_of_msg, messages, intervals)
            choice = input("\nDo you want to send more messages (y/n): ")
            if (choice == "n" or choice == "q"):
                break
    except Exception as e:
        print("\nInvalid input, Enter 'q' to exit")

if __name__ == '__main__':
    driver = ''
    templink = ''
    main()