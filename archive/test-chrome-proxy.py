from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "106.1.18.35:8080"
proxy.socks_proxy = "106.1.18.35:8080"
proxy.ssl_proxy = "106.1.18.35:8080"

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

#capabilities.add_experimental_option('androidPackage', 'com.android.chrome')
#capabilities.androidPackage = 'com.android.chrome'

driver = webdriver.Chrome(desired_capabilities=capabilities)
