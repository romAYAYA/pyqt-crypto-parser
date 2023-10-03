import requests
from bs4 import BeautifulSoup


class Currency:
    def __init__(self, name: str, symbol: str, price_usd: float):
        self.name = name
        self.symbol = symbol
        self.price_usd = price_usd


# async def async_requests(url: str, headers: dict) -> any:
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url=url, headers=headers) as response:
#             data = await response.read()
#             return json.loads(data)
#
#
# def get_currency(url: str, search: str, filter_q: str) -> list[Currency]:
#     """
#      Decomposition:
#      1. Get data from a site
#      2. Filter data by parameters (search, filter_q)
#      3. Serialize (JSON -> python OBJ)
#      """


def core():
    url = 'https://www.coingecko.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers).text

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        title: article.find('h2').text
        link = article.find('a')['href']


if __name__ == '__main__':
    core()
