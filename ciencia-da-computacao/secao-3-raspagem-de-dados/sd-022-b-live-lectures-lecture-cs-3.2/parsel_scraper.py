from parsel import Selector
import requests


def fetch_content(url: str, wait: int = 1) -> str:
    try:
        # fazenda a requisita pela url com um timeout de limite
        response = requests.get(url, timeout=wait)
        # espera pelo codigo de erro para tratá-lo
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    # com a resposta da requisição eu mando apenas o texto(html) da resposta
    return response.text


def extract_quotes(content: str) -> list[dict]:
    # cria uma instancia dos seletores do parsel
    selector = Selector(content)
    # atributo onde receberei meus filtros de busca
    quotes = []
    # com o selector.css => busco apenas o elemento referido pelos 
    # atributos css
    for quote in selector.css('div.quote'):
        # busca todos os elementos filhos de quote que sejam span 
        # com atributo tipo text e pega o texto do primeiro elemento 
        text = quote.css('span.text::text').get()
        # busca a tag small com atributo author e pega o texto do 
        # primeiro atributo
        author = quote.css('small.author::text').get()
        # busca pela tag a com atributo tag e captura o texto de todos
        #  os elementos
        tags = quote.css('a.tag::text').getall()
        # adiciona à lista quote um objeto contendo as chaves: 
        # text, author, tags
        quotes.append(
            {
                'text': text,
                'author': author,
                'tags': tags
            }
        )

    return quotes


# função que busca a próxima página
def get_next_page(content: str) -> str:
    selector = Selector(content)
    next_page = selector.css('li.next > a::attr(href)').get()
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
    print(quotes)
