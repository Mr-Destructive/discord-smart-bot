import os
import sys

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
from bot_init import train_bot
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

# Create spam logs
def create_logs(logs):
    localtime = time.localtime()
    timeStamp = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
    
    with open(f'logs/{timeStamp}.txt', 'w') as file:
        for log in logs:
            file.write(log)
            file.write("\n")

# Starting spam
def chat(n, intervals, chatbot):
    logs = []
    
    system('cls' if osname == 'nt' else 'clear')
    with alive_bar(n, title='Chatting', bar='classic2', spinner='classic') as bar:
        for i in range(n):
            localtime = time.localtime()
            timeStamp = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
    
            randomTime = random.choice(intervals)
            
            while True:
                thread = driver.find_elements_by_class_name('messageContent-2qWWxC')
                try:
                    while not thread[-1] == None:
                        break
                    break
                except Exception as e:
                    print(e)
                    pass
            response = chatbot.get_response(thread[-1].text)
            
            actions = ActionChains(driver)
            actions.send_keys(response.text)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            bar()
            sleep(randomTime)
            
            logs.append(f'{str(i).zfill(3)} - {randomTime}s - {timeStamp} - {response}')
    print("\nAll Messages Sent")
    create_logs(logs)

# Menu
def main():
    global flag
    flag = False
    intervals = []
    time_interval = ""

    details = retrieve_credentials()
    chatbot = train_bot()
    
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
            chat(num_of_msg, intervals, chatbot)
            choice = input("\nDo you want to send more messages (y/n): ")
            if (choice == "n" or choice == "q"):
                break
    except Exception as e:
        print("\nInvalid input, Enter 'q' to exit")

if __name__ == '__main__':
    driver = ''
    templink = ''
    main()