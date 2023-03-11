from bs4 import BeautifulSoup
import requests


def fetch_content(url: str, wait: int = 1) -> str:
    try:
        response = requests.get(url, timeout=wait)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""

    return response.text


def extract_quotes(content: str) -> list[dict]:
    soup = BeautifulSoup(content, "html.parser")

    quotes = []
    for quote in soup.find_all('div', {'class': 'quote'}):
         text = quote.find('span', class_='text').text
         author = quote.find('small', class_='author').text
         tags = [
            tag.text
            for tag in quote.find_all('a', class_='tag')
         ]
         quotes.append(
              {
                'text': text,
                'author': author,
                'tags': tags
              }
         )

    return quotes


def get_next_page(content: str) -> str:
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.select('li.next > a')
    next_page = links[0]['href'] if links else ""
    return next_page

def get_all_quotes() -> list[dict]:
    base_url = "https://quotes.toscrape.com"
    next_page = "/"
    quotes = []
    while next_page:
        url = base_url + next_page
        print(f"Scraping {url}")

        content = fetch_content(url)
        quotes.extend(
            extract_quotes(content)
        )

        next_page = get_next_page(content)

    return quotes


if __name__ == '__main__':
	quotes = get_all_quotes()
	# print(quotes)