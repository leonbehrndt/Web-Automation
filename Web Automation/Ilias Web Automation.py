from selenium.common import exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep


## Open Chrome Browser
chrome = webdriver.Chrome()
# Open ILIAS
url = "https://ilias3.uni-stuttgart.de/login.php?target=root_1&client_id=Uni_Stuttgart&cmd=force_login&lang=en"
chrome.get(url)

## Open everything until class Selection
user = "st180237"
userInputForm = chrome.find_element_by_xpath('//*[@id="username"]').send_keys(user)

password = "8$31j3568v0"
passwordInputForm = chrome.find_element_by_xpath('//*[@id="password"]').send_keys(password)

loginButton = chrome.find_element_by_xpath('//*[@id="form_"]/div/div[4]/div[2]/input').click()

myCoursesButton = chrome.find_element_by_xpath('/html/body/div[2]/div[3]/div/nav/div[2]/ul/li[2]/a').click()

## Choose Lecture
openLecturePage_PSE = chrome.find_element_by_xpath('//*[@id="block_pdmem_0"]/div/div[2]/div/div[4]/div/div/div[2]/div[1]/a').click()

openLectureScriptsPage_PSE = chrome.find_element_by_xpath("/html/body/div[1]/main/div/div/div/div/div/div[3]/div[3]/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[1]/h3/a").click()

'''
Searches for a specific container to iterate through.
Iterates through a specific 
'''
def iterateOverHLinks(containerPath, itemPath):
    lectureScriptsContainer = chrome.find_element_by_xpath(containerPath)
    scriptNames = lectureScriptsContainer.find_elements_by_xpath(itemPath)
    o = Options()

    ## Go through folders
    for i, name in enumerate(scriptNames):
        lectureScriptsContainer = chrome.find_element_by_xpath(containerPath)
        scriptNames = lectureScriptsContainer.find_elements_by_xpath(itemPath)
        name = scriptNames[i]
        name.click()

        ## Go through scripts after opening folder
        scriptsContainer = chrome.find_element_by_xpath(containerPath)
        scripts = scriptsContainer.find_elements_by_xpath(itemPath)
        for j, script in enumerate(scripts):
            scriptsContainer = chrome.find_element_by_xpath(containerPath)
            scripts = scriptsContainer.find_elements_by_xpath(itemPath)
            script = scripts[j]
            script.click()
            # TODO: Downloading page after opening
            
        chrome.back()
    
    ## Go through tabs to download items
    windows = chrome.window_handles
    for k, window in enumerate(windows):
        if window is not windows[0]:
            chrome.switch_to.window(windows[k])
            chrome.close()
        else:
            continue

        
iterateOverHLinks('//*[@class="ilContainerItemsContainer "]', '//a[@class="il_ContainerItemTitle"]')
