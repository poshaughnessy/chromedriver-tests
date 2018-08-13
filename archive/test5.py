# v8 example from the wiki
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('androidPackage', 'com.sec.android.app.sbrowser')
options.add_experimental_option('androidActivity', '.SBrowserMainActivity')
options.add_experimental_option('androidDeviceSocket', 'Terrace_devtools_remote')
options.add_experimental_option('androidExecName', 'Terrace')

# Adding device serial is needed only when you tests multi-devices
# In terminal, type "adb devices", and you find device serial.
# options.add_experimental_option('androidDeviceSerial', 'ce051715d0f3ee21047e')

# First argument is chromedriver real path.
driver = webdriver.Chrome('/Users/peter/dev/lib/chromedriver/2.36/chromedriver', chrome_options=options)

# move to google.
driver.get('http://google.com')

# You can find element ID, xpath in Chrome F12 devtools mode.
# 1. Right mouse click on thing you want to control.
# 2. Inspect and right mouse click that text part.
# 3. Copy -> copy by xpath, selector(name).
# 4. Then put it in like below.

driver.find_element_by_name('q').send_keys('Selenium python example')
driver.find_element_by_xpath("""//*[@id="tsf"]/div[2]/div[1]/div[1]/button""").click()
