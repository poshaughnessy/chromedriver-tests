from selenium import webdriver
capabilities = {
  'chromeOptions': {
    'androidPackage': 'com.sec.android.app.sbrowser',
    'androidActivity': 'SBrowserMainActivity',
    'androidDeviceSocket': 'Terrace_devtools_remote',
    'androidExecName': 'Terrace'
  }
}
driver = webdriver.Remote('http://localhost:9515', capabilities)
driver.get('http://samsung.com')
driver.quit()
