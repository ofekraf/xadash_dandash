import requests
from bs4 import BeautifulSoup
import pickle



def main():
    haaretz_url = "https://www.haaretz.co.il/"

    # Get the HTML content of the Haaretz website
    response = requests.get(haaretz_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all links to articles on the Haaretz website
    article_links = [link.get('href') for link in soup.find_all('a') if 'https://promotions.haaretz.co.il/' not in link]


    # Create a dictionary to store the word count and article lists
    word_dict = {}

    # Loop through each article link and extract the text
    for link in article_links:
        # Get the HTML content of the article
        article_response = requests.get(link)
        article_soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the article text and tokenize it into words
        body = article_soup.find('div', {'class': 'article-body'})
        if not body:
            continue
        words = body.get_text().split()


        # Update the word count and article lists in the dictionary
        for word in words:
            if word not in word_dict:
                word_dict[word] = {
                    'count': 1,
                    'articles': [link]
                }
            else:
                word_dict[word]['count'] += 1
                if link not in word_dict[word]['articles']:
                    word_dict[word]['articles'].append(link)


    # Save the dictionary as a file
    with open('word_dict.pkl', 'wb') as f:
        pickle.dump(word_dict, f)

if __name__ == '__main__':
    main()