import bs4
from selenium import webdriver
def MoHA_Directory(URL):
    driver_firefox=webdriver.Firefox(executable_path="C:\\Selenium Driver\\geckodriver.exe")
    driver_firefox.get(URL)
    search=driver_firefox.find_element_by_css_selector("#pro_helper_form > div > div > div.col-md-2.col-lg-2.float-right > button")     #CSS Selector for Search in the Directory
    search.click()      #Click Search to get all the numbers in the Directory
    html=driver_firefox.page_source
##    print(html)
    soup=bs4.BeautifulSoup(html,"html.parser")
    d=soup.find_all(r'#app > div.container > div > table > tbody > tr:nth-child(1) > td:nth-child(6)')
    print(d)
    return (d)
MoHA_Directory("http://moha.gov.np/en/directory")

    
