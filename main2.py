from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time
from pathlib import Path
import winreg


def baslangic():
    global skillcappedlink
    print("""

 _____ _    _ _ _ _   _                                      _ 
/  ___| |  (_) | | | | |                                    | |
\ `--.| | ___| | | | | |_ __   ___ __ _ _ __  _ __   ___  __| |
 `--. \ |/ / | | | | | | '_ \ / __/ _` | '_ \| '_ \ / _ \/ _` |
/\__/ /   <| | | | |_| | | | | (_| (_| | |_) | |_) |  __/ (_| |
\____/|_|\_\_|_|_|\___/|_| |_|\___\__,_| .__/| .__/ \___|\__,_|
                                       | |   | |               
                                       |_|   |_|               

""")
    skillcappedlink = input("Enter the Link \n")
    global dosya_ismi
    dosya_ismi = input("Name of the Folder \n")
    print("""
  ____                      _                 _   ____  _             _           _ 
 |  _ \  _____      ___ __ | | ___   __ _  __| | / ___|| |_ __ _ _ __| |_ ___  __| |
 | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` | \___ \| __/ _` | '__| __/ _ \/ _` |
 | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  ___) | || (_| | |  | ||  __/ (_| |
 |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| |____/ \__\__,_|_|   \__\___|\__,_|
                                                                                    
""")
    finddownlaod()
    linkiSik(skillcappedlink)
    websiteac(skillcappedlink)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')




def finddownlaod():
    if os.name == 'nt':
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            global location
            location = winreg.QueryValueEx(key, downloads_guid)[0]



def linkiSik(link):
    sperm_ve_yumurta = link.split('course/')[1]
    dollenmis_id = sperm_ve_yumurta.split('/')[0]
    global masallahi_olan_id
    masallahi_olan_id = 'BrVidRow-' + dollenmis_id
    
def websiteac(link):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    global driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)
    try:
     course = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[3]/div[7]/div/div/div[3]/div[1]/div[1]/div/div[1]"))
    )
    finally:
        course.click()
    time.sleep(2)
    search = driver.find_element(By.ID,masallahi_olan_id)
    global datalar
    datalar = driver.find_elements(By.CLASS_NAME,search.get_attribute('class'))
    datacekme(datalar)



def shorten_strings(input_text):
    input_list = input_text.split("\n")
    output_list = []
    for string in input_list:
        shortened_string = string[:-10].replace("browse3/", " ")
        output_list.append(shortened_string)
    global output_text
    output_text = "\n".join(output_list)
    output_text = output_text[:-1]

def datacekme(datalar):
    numara = 1
    locate()
    global isimler
    isimler = set()
    for data in datalar:
        data.click()
        link = driver.current_url
        global isim
        isim = driver.find_element(By.XPATH,f"/html/body/div[2]/div/div[3]/div[7]/div/div/div[3]/div[2]/div[{numara}]/div/div[1]/div[2]/div/div[1]").get_attribute('innerText')
        isimler.add(isim + ".ts")
        time.sleep(1)
        driver.execute_script("window.open('');")
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1]) 
        driver.get("file://" + new_website)
        time.sleep(1.5)
        shorten_strings(link)
        driver.find_element(By.ID,'url').send_keys(output_text)
        driver.find_element(By.ID,"videoName").send_keys(isim)
        driver.find_element(By.XPATH,'/html/body/div/button').click()
        numara +=1
        while driver.find_element(By.ID,'status').get_attribute('innerText') != "DONE":
            time.sleep(1)
        time.sleep(0.5)
        driver.switch_to.window(driver.window_handles[0])
    print(isimler)
    driver.quit()
    dosyaya_koymaca()

def locate():
    for r,d,f in os.walk("c:\\"):
        for files in f:
            if files == "annen.html":
                website = os.path.join(r,files)
                break
    for i in range(len(website)):
        if website[i] == "\\":
            global new_website
            new_website= website.replace(website[i],"/")
    new_website = new_website[0].upper() + new_website[1:]

def dosyaya_koymaca():
    os.makedirs(dosya_ismi)
    for r,d,f in os.walk(location):
        for files in f:
            if str(files) in isimler:
                    file_pathway = str(os.path.join(location,files))
                    os.replace(file_pathway,os.getcwd() + "\\" + dosya_ismi + "\\" + files)
    cls()
    print(""""
  _____ _       _     _              _ 
 |  ___(_)_ __ (_)___| |__   ___  __| |
 | |_  | | '_ \| / __| '_ \ / _ \/ _` |
 |  _| | | | | | \__ \ | | |  __/ (_| |
 |_|   |_|_| |_|_|___/_| |_|\___|\__,_|
                                       
""")

                

if __name__ == "__main__":
    baslangic()
