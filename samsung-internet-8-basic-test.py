# Basic example of running Samsung Internet v8.x using ChromeDriver v2.36
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('androidPackage', 'com.sec.android.app.sbrowser')
options.add_experimental_option('androidActivity', '.SBrowserMainActivity')
options.add_experimental_option('androidDeviceSocket', 'Terrace_devtools_remote')
options.add_experimental_option('androidExecName', 'Terrace')

# NB. chromedriver will need to be in your path! (Or change this to your specific path)
driver = webdriver.Chrome('chromedriver', chrome_options=options)

# Load a website
driver.get('https://www.samsung.com/uk/')
