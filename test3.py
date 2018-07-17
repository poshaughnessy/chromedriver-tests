from selenium import webdriver

# NB. It works without any options - it fires up Chrome desktop browser
options = webdriver.ChromeOptions()
#options.add_experimental_option('androidPackage', 'com.sec.android.app.sbrowser')
#options.add_experimental_option('androidActivity', 'SBrowserMainActivity')
#options.add_experimental_option('androidDeviceSocket', 'Terrace_devtools_remote')
#options.add_experimental_option('androidExecName', 'Terrace')

# In terminal, type "adb devices", and you find device serial.
#If you have only one device, then no need to add DeviceSerial
#options.add_experimental_option('androidDeviceSerial', 'FA7AH1A02477')

# First argument is chromedriver real path. (out/Release/chromedriver)
driver = webdriver.Chrome('/home/SERILOCAL/p.oshaughnes/dev/lib/ChromeDriver/chromedriver', chrome_options=options)

# move to google.
driver.get('http://google.com')
