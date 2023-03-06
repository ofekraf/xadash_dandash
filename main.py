import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from constants import *


def main():
    initial_crawl()

def initial_crawl():
    if not INITIAL_CRAWL:
        return False

    # Create a new Chrome driver instance
    driver = webdriver.Chrome()

    # Navigate to the committee protocols page
    url = 'https://main.knesset.gov.il/Activity/committees/Pages/AllCommitteeProtocols.aspx'
    driver.get(url)

    # Wait for the page to load completely
    driver.implicitly_wait(10)

    # Get the HTML content of the page
    html = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the links to the committee protocol pages
    committee_links = []
    for link in soup.select('a[href^="/committees/protocol"]'):
        committee_links.append('https://main.knesset.gov.il' + link['href'])

    # Loop through the committee protocol links and extract the words spoken
    all_words = []
    for link in committee_links:
        driver.get(link)
        driver.implicitly_wait(10)
        html = driver.page_source
        session_soup = BeautifulSoup(html, 'html.parser')
        session_words = session_soup.find_all('span', {'class': 'pspeaker_word'})
        for word in session_words:
            all_words.append(word.text.strip())

    # Print all the words spoken in committee protocols
    print(all_words)

    # Quit the driver
    driver.quit()

if __name__ == '__main__':
    main()