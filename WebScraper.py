from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
startUrl ="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome('Driver/chromedriver')
browser.get(startUrl)
time.sleep(10)
def scrape():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planetdata = []
    for i in range (0,428):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ultag in soup.find_all("ul",attrs = {"class","exoplanet"}):
            litags = ultag.find_all("li")
            templist = []
            for index,litag in enumerate(litags):
                if index == 0:
                    templist.append(litag.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(litag.contents[0])
                    except:
                        templist.append("")
            planetdata.append(templist)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("MyScrapedData.csv","w")as f:
        csvwriter = csv.writer(f)
        csv.writer.writerow(headers)
        csv.writer.writerows(planetdata)
scrape()