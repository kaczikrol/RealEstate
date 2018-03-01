from OnlineAuctionsList import OnlineAuctions as auctions
from urllib import request, error
from bs4 import BeautifulSoup as soup
from AuctionClass import Auction
from collections import namedtuple
import csv

def AuctionsData():
    auction_list = auctions()
    auction_list_html = []
    auctions_object = []
    for page in auction_list:
        try:
            u_client = request.urlopen(page)
            auction_list_html.append(u_client.read())
            u_client.close()
        except error.URLError as e:
            print('Failed reach to server, reason: ', e.reason)


    for index in range(0, len(auction_list)):
        test = Auction(auction_list_html[index], auction_list[index])
        auctions_object.append(test)


    with open("real_estate_data.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        title_tuple = ("URL", "LOKALIZACJA", "NAGŁOWEK", "CENA", "CENA_M2", "POWIERZCHNIA", "POKOJE", "PIĘTRO",
                       "RYNEK", "RODZAJ_BUDYNKU", "MATERIAŁ", "OKNA", "OGRZEWANIE", "ROK_BUDOWY", "STAN_WYKOŃCZENIA",
                       "CZYNSZ", "FORMA_WŁASNOŚCI", "MEDIA", "ZABEZPIECZENIA", "WYPOSAŻENIE", "INFO_DODATKOWE",
                       "DZIELNICA", "DOSTEPNE_OD")
        writer.writerow(title_tuple)
        for data in auctions_object:
            data_tuple = (data.url, data.location, data.header, data.price, data.price_per_m2, data.area,
                          data.rooms, data.floor, data.market, data.form_of_house, data.bulid_material, data.windows,
                          data.heating, data.year_of_build, data.trim_condition, data.rent, data.owernship_form,
                          data.media, data.protection, data.equipment, data.additionaly_info, data.district,
                          data.avaiable_from)
            writer.writerow(data_tuple)

    return 0
AuctionsData()


