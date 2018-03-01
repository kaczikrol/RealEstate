from bs4 import BeautifulSoup as soup


class Auction():
    def __init__(self, html, url):
        self.soup = soup(html,"html.parser")
        self.url = url
        self.header = self.header()
        self.location = self.location()
        self.price = self.price()
        self.price_per_m2 = self.price_per_m2()
        self.area = self.area()
        self.rooms = self.rooms()
        self.floor = self.floor()
        self.market = self.market()
        self.form_of_house = self.form_of_house()
        self.bulid_material = self.build_material()
        self.windows = self.windows()
        self.heating = self.heating()
        self.year_of_build = self.year_of_build()
        self.trim_condition = self.trim_condition()
        self.rent = self.rent()
        self.owernship_form = self.owernship_form()
        self.media = self.media()
        self.protection = self.protection()
        self.equipment = self.equipment()
        self.additionaly_info = self.additionaly_info()
        self.district = self.district()
        self.avaiable_from = self.avaiable_from()
        self.headers_list = self.headers_list()

    @staticmethod
    def CleaningStringToFloat(string):
        try:
            value = ""
            for char in string:
                if char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.'):
                    if char == ',':
                        char = '.'
                    value = str(value) + (str(char))
            return value
        except:
            return string

    @staticmethod
    def FindDynamicCharacteristic(soup, characteristic):
        try:
            sub_list = soup.findAll("ul", {"class" : "sub-list"})
            sub_list = sub_list[0].findAll("li")
            for index in range(0,len(sub_list)):
                if sub_list[index].strong.text == characteristic:
                    return str(str(sub_list[index].text).replace(characteristic+" ", ""))

        except:
            return None

    @staticmethod
    def HeaderIndicator(headers_list, characteristic):
        try:
            for index in range(0, len(headers_list)):
                if headers_list[index] == characteristic:
                    return int(index)
        except:
            return None


    def HeaderListData(self, characteristic):
        try:
            header_list_data = []
            headers_list = self.headers_list()  #we cannot takes attr self.headers_list because list is mutable and then in index we have None because of reference to memory
            header_list_data_temp = self.soup.findAll("ul", {"class" : "dotted-list"})
            index = Auction.HeaderIndicator(headers_list, characteristic)
            header_list_data_temp = header_list_data_temp[index].findAll("li")
            for element in header_list_data_temp:
                header_list_data.append(element.text.strip())
            return header_list_data
        except:
            return None


    def header(self):
        try:
            title = self.soup.findAll("h1", {"itemprop" : "name"})
            return title[0].text
        except:
            return None

    def location(self):
        try:
            location = self.soup.findAll("p", {"class" : "address-text"})
            return location[0].text
        except:
            return None

    def price(self):
        try:
            price = self.soup.findAll("ul", {"class" : "main-list"})
            price = price[0].findAll("li",{"class" : "param_price"})
            price = price[0].strong.text
            price = Auction.CleaningStringToFloat(price)
            return float(price)
        except:
            return None


    def price_per_m2(self):
        try:
            price_m2 = self.soup.findAll("ul", {"class" : "main-list"})
            price_m2 = price_m2[0].findAll("li",{"class" : "param_price"})
            price = str(price_m2[0].span)
            price_m2 = str(price_m2)
            price_m2 = price_m2.replace(price,"")
            price_m2 = Auction.CleaningStringToFloat(price_m2)
            return float(price_m2)
        except:
            return None

    def area(self):
        try:
            area = self.soup.findAll("ul", {"class" : "main-list"})
            area = area[0].findAll("li", {"class" : "param_m"})
            area = area[0].strong.text
            area = Auction.CleaningStringToFloat(area)
            return float(area)
        except:
            return None

    def rooms(self):
        try:
            rooms = self.soup.findAll("ul", {"class" : "main-list"})
            rooms = rooms[0].findAll("li")
            rooms = rooms[2].text
            rooms = Auction.CleaningStringToFloat(rooms)
            return int(rooms)
        except:
            return None

    def floor(self):
        try:
            floor = self.soup.findAll("ul", {"class" : "main-list"})
            floor = floor[0].findAll("li", {"class" : "param_floor_no"})
            floor = floor[0].strong.text
            return int(floor)
        except:
            return None

    def market(self):
        return Auction.FindDynamicCharacteristic(self.soup, "Rynek:")

    def form_of_house(self):
        return Auction.FindDynamicCharacteristic(self.soup, "Rodzaj zabudowy:")

    def build_material(self):
        return Auction.FindDynamicCharacteristic(self.soup, "Materiał budynku:")

    def windows(self):
        return Auction.FindDynamicCharacteristic(self.soup, "Okna:")

    def heating(self):
        return Auction.FindDynamicCharacteristic(self.soup, "Ogrzewanie:")

    def year_of_build(self):
        return Auction.FindDynamicCharacteristic(self.soup, "Rok budowy:")

    def trim_condition(self):
        return Auction.FindDynamicCharacteristic(self.soup, "Stan wykończenia:")

    def rent(self):
        try:
            return float(Auction.CleaningStringToFloat(Auction.FindDynamicCharacteristic(self.soup, "Czynsz:")))
        except:
            return Auction.CleaningStringToFloat(Auction.FindDynamicCharacteristic(self.soup, "Czynsz:"))

    def owernship_form(self):
        return Auction.FindDynamicCharacteristic(self.soup, "Forma własności:")

    def media(self):
        try:
            media = self.HeaderListData("Media")
            return media
        except:
            return None

    def protection(self):
        try:
            protection = self.HeaderListData("Zabezpieczenia")
            return protection
        except:
            return None

    def equipment(self):
        try:
            equipment = self.HeaderListData("Wyposażenie")
            return equipment
        except:
            return None

    def additionaly_info(self):
        try:
            equipment = self.HeaderListData("Informacje dodatkowe")
            return equipment
        except:
            return None

    def district(self):
        district_list = ['Antoninek','Zieliniec','Kobylepole','Chartowo','Fabianowo','Kotowo','Główna','Głuszyna',
                     'Górczyn','Grunwald','Jana III Sobieskiego','Jeżyce','Junikowo','Kiekrz','Krzesiny','Pokrzywno',
                     'Garaszewo','Krzyżowniki','Smochowice','Kwiatowe','Ławica','Morasko','Radojewo','Naramowice',
                     'Winogrady','Ogrody','Ostrów Tumski','Śródka','Zawady','Komandoria','Piątkowo','Podolany',
                     'Rataje','Sołacz','Stare Miasto','Stare Winogrady','Starołęka','Minikowo','Marlewo',
                     'Stary Grunwald','Strzeszyn','Szczepankowo','Spławie','Krzesinki','Łazarz','Świerczewo',
                     'Umultowo','Warszawskie','Pomet','Maltańskie','Wilda','Winiary','Wola','Zielony Dębiec',
                     'Żegrze','Dębiec']
        try:
            for dist in district_list:
                if dist in self.location:
                    return dist
        except:
            return None

    def avaiable_from(self):
        return Auction.FindDynamicCharacteristic(self.soup, "Dostępne od:")

    def print_html(self):
        print(self.soup)

    def headers_list(self):
        headers_list = []
        h4 = self.soup.findAll("h4")
        for index in range(0, len(h4)):
            if h4[index].text in ("Media", "Zabezpieczenia", "Wyposażenie", "Informacje dodatkowe"):
                headers_list.append(h4[index].text)
        return list(headers_list)

