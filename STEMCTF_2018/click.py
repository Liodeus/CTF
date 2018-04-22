from selenium import webdriver

url = "http://138.247.115.170/"

mydriver = webdriver.Firefox()
mydriver.get(url)

while True:
	mydriver.find_element_by_css_selector('a').click()

mydriver.quit()
