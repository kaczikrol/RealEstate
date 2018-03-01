from bs4 import BeautifulSoup as soup
from urllib import  request

def OnlineAuctions():

    number_of_pages = 172
    urls =[]
    for i in range(1, number_of_pages+1):
        urls.append("https://www.otodom.pl/sprzedaz/mieszkanie/poznan/?search[description]=1&search[dist]=0&search[subregion_id]=462&search[city_id]=1&page=%s" %i)

    pages_html = []
    for url in urls:
        u_client = request.urlopen(url)
        pages_html.append(u_client.read())
        u_client.close()


    auctions = []   #jak nie pyknie to to trzeba zmienic
    for page_html in pages_html:
        page_soup = soup(page_html, "html.parser")
        header_page_soup = page_soup.findAll("header", {"class" : "offer-item-header"})
        for index in range(0, len(header_page_soup)):
            header_page_url = header_page_soup[index].a['href']
            auctions.append(header_page_url.strip())


    print(auctions)
    return auctions

OnlineAuctions()
