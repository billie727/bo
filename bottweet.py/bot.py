from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome(executable_path="/Users/BotTp8/Downloads/chromedriver")
driver.get("https://twitter.com/")
sleep(3)
driver.find_element_by_name('session[username_or_email]').send_keys("BotTp8")
driver.find_element_by_name('session[password]').send_keys("elbot2121727")
driver.find_element_by_name('session[password]').send_keys(Keys.RETURN)
sleep(3)

f = open("MTV.txt", 'r')

for word in f:
    if word == "\n":
        continue
        driver.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
        sleep(1)
        drive.find_element_by_class_name('notranslate').click()
        driver.find_element_by_cass_name('notranslate').send_keys(word)
        driver.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
        sleep(10)

        f.close()



