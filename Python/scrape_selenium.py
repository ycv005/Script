import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import wget
import pandas as pd
import requests 

def main(Keyword):
    urlpage = 'https://bestpractice.bmj.com/login' 
    # print(urlpage)
    # run firefox webdriver from executable path of your choice
    driver = webdriver.Firefox()

    driver.maximize_window()
    # get web page
    driver.get(urlpage)

    cookies = {
        'sessionhash': driver.get_cookie('sessionhash'),
    }
    user_agent = driver.execute_script("return navigator.userAgent;")
    headers = {
        'User-Agent': user_agent,
    }
    # execute script to scroll down the page
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    driver.execute_script("window.scrollTo(0, 300)");

    # if "bmj" in url:
    username = driver.find_element_by_name("lfInputEmail") #username form field
    password = driver.find_element_by_name("lfInputPass") #password form field

    username.send_keys("Library@hindujahospital.com")
    password.send_keys("LIB123#")

    submitButton = driver.find_element_by_id("loginSubmit")    
    submitButton.click()

    time.sleep(4)   #sleep for the form submission
    driver.get("https://bestpractice.bmj.com/")
    time.sleep(1)

    searchBar = driver.find_element_by_id("q")
    searchButton = driver.find_element_by_id("mainSearchBtn")

    searchBar.send_keys(Keyword)
    searchButton.click()

    driver.execute_script("window.scrollTo(0, 200)");
    innerHTML = driver.execute_script("return document.body.innerHTML") #returns the inner HTML as a string

    # print(innerHTML)
    if "No results found for" in innerHTML:
        soup = BeautifulSoup(innerHTML)
        for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
            print(link.get('href'))


    soup = BeautifulSoup(innerHTML)
    links = []
    numbers = []

    for link in soup.findAll('a'):
        l = link.get('href')
        if isinstance(l, str):
            n = l.split("/")
            for eachn in n:
                if eachn.isdigit() == True:
                    if int(eachn) not in numbers:
                        numbers.append(int(eachn))
            if "topics/en-gb/" in l and "pdf" in l:
                links.append(l)


    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 1);
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    # fp.set_preference("browser.download.dir", "/home/")
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/pdf')
    # fp.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
    fp.set_preference("pdfjs.disabled", True)


    i=0
    for l in numbers:
        url = "https://bestpractice.bmj.com/topics/en-gb/" + str(l) + "/pdf/" + str(l)+ ".pdf"
        driver.get(url)
        if i<0:
            username = driver.find_element_by_name("lfInputEmail") #username form field
            password = driver.find_element_by_name("lfInputPass") #password form field

            username.send_keys("Library@hindujahospital.com")
            password.send_keys("LIB123#")

            submitButton = driver.find_element_by_id("loginSubmit")    
            submitButton.click()

        time.sleep(4)
        try:
            driver.find_element_by_id("download").click()
        except:
            print("No Documents Found")
            continue
            print("will not printed")

        time.sleep(10)
        i+=1

    time.sleep(10)
    driver.quit()

Keyword = "Acute lymphocytic leukaemia"
main(Keyword)
