from selenium import webdriver
import httplib

capabilities = {
  'chromeOptions': {
    'androidPackage': 'com.android.chrome',
    'androidUseRunningApp': True
  }
}

try:
  webdriver.Remote('http://127.0.0.1:9515', capabilities)
  driver.get('https://www.samsung.com/uk/')
  #driver.quit()

  #driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
  #driver.get('https://www.samsung.com/uk/');


except httplib.BadStatusLine as bsl:
  print(bsl)
