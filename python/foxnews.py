from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class FoxNewsArticle:
    topic = ""
    title = ""
    link = ""


def GrabFoxArticles():
    options = Options()
    options.add_argument("headless")
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.foxnews.com/")
    ListOfArticles = driver.find_elements(By.XPATH, "//article//h2//a")
    del ListOfArticles[0:10:1]
    FoxNewsArticles = []

    driver.execute_script("window.scrollTo(0,3000)")

    for i in range(len(ListOfArticles)):
        tempArticle = FoxNewsArticle()
        tempArticle.topic = "N/A"
        tempArticle.title = ListOfArticles[i].text
        tempArticle.link = ListOfArticles[i].get_attribute("href")
        FoxNewsArticles.append(tempArticle)

    driver.close()

    return FoxNewsArticles


def SearchArticles(listOfArticles, keyword):
    desiredArticles = []
    for article in listOfArticles:
        if keyword.lower() in article.title.lower():
            desiredArticles.append(article)

    return desiredArticles
