from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('androidPackage', 'com.android.chrome')
driver = webdriver.Chrome('/home/SERILOCAL/p.oshaughnes/dev/lib/ChromeDriver/chromedriver', chrome_options=options)
driver.quit()
