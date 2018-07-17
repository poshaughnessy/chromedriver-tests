from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('androidPackage', 'com.sec.android.app.sbrowser')

# In terminal, type "adb devices", and you find device serial.
#If you have only one device, then no need to add DeviceSerial
#options.add_experimental_option('androidDeviceSerial', 'ce051715d0f3ee21047e')

# First argument is chromedriver real path. (out/Release/chromedriver)
driver = webdriver.Chrome('/home/SERILOCAL/p.oshaughnes/dev/lib/ChromeDriver/chromedriver', chrome_options=options)

# move to google.
driver.get('http://google.com')
