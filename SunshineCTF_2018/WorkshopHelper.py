from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time

url = "http://workshop.web1.sunshinectf.org/"

mydriver = webdriver.Firefox()
mydriver.get(url)
mydriver.find_element_by_xpath("(//*[text()='Start'])[1]").click()

time.sleep(0.8)

while True:
	time.sleep(1)
	pageSoup = soup(mydriver.page_source, "html.parser")

	question = pageSoup.find("h1", {"id": "question"}).text

	q1 = question.split(' ')[-3]
	q2 = question.split(' ')[-1]

	find = mydriver.find_element_by_xpath("//*[@{}='{}']".format(q1, q2))
	split = find.text.split()
	answer = str(int(eval("{}{}{}".format(split[0], split[1], split[2]))))

	try:
		find.find_element_by_name("input").send_keys(answer)
	except:
		for x in find.find_elements_by_xpath(".//input"):
			if  x.get_attribute("text") == answer:
				x.click()
				break

	find.find_element_by_tag_name("button").click()

time.sleep(10)
mydriver.quit()

