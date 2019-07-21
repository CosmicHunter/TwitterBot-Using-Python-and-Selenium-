from selenium import webdriver

# we have installed gecko driver (so whenever we run our python script/app
# this gecko driver is going to open a firefox browser

#Selenium requires a web driver to interface with the chosen browser.
# Web drivers is a package to interact with web browser. It interacts with the
#web browser or a remote web server through a wire protocol which is
# common to all. You can check out and install the web drivers of your browser choice.

from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()   # creating an instance of a webdriver named bot

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3) # just to stop the app for 3 seconds in order to wait for the webpage to load
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()    # we do this to make sure that the email and password fields are empty
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')

        # the .get() method loads the webpage in the browser and waits for the
        # webpage to completely load and return the control back to the test script once
        # the webpage is loaded
        time.sleep(3) # waiting time for webpage to load

        # We after loading a particular hashtag we also want the bot to scroll down and load
        # a decent amount of tweets and like them
        # for this we will use some JavaScript
        #bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        # We can run this command multiple times so we are going to add it in a
        # loop

        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            # now we can search for each tweet
            tweets = bot.find_elements_by_class_name('tweet')
            links=[i.get_attribute('data-permalink-path')
                   for i in tweets]
            #print(links)
            for j in links:   # we need to open each individual link
                bot.get('https://twitter.com'+j)
                try:
                    bot.find_elements_by_class_name('HeartAnimation').click()
                    time.sleep(3)  # else twitter will detect abnormal activity
                except Exception as ex:
                    time.sleep(60)



           # print(links)

# Next, we are sending keys, this is similar to entering keys using your
# keyboard. Special keys can be sent using Keys class imported from
# selenium.webdriver.common.keys. To be safe, we’ll first clear any
# pre-populated text in the input field (e.g. “Search”) so it doesn’t affect
# our search results:




botobject = TwitterBot('GroddSolovar','twitterbot')
botobject.login()
botobject.like_tweet('WebDevelopment')

