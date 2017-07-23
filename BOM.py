import requests
from bs4 import BeautifulSoup
#extracts weather data from http://bom.gov.au
main_address = "http://www.bom.gov.au/products/"
search_address = "http://www.bom.gov.au/"

fields = {
    "Date/Time":0,
    "Temp":1,
    "App Temp":2,
    "Dew Point":3,
    "Rel Hum":4,
    "Delta T":5,
    "Dir":6,
    "Spd km/h":7,
    "Gust km/h":8,
    "Spd kts":9,
    "Gust kts":10,
    "Press QNH":11,
    "Press MSL":12,
    "Rain since 9am":13
}

class ExtractBOM:
    def __init__(self,Region, Area, Location):
        self.Region = Region.lower()
        self.Area = Area.lower()
        self.Location = Location
        load_out = BeautifulSoup(requests.get(search_address+Region+"/observations/"+Area+".shtml").text, 'html.parser')
        links = load_out.findAll("a")
        self.address = None
        for link in links:
            if link.text == Location:
                self.address = search_address + link['href']
                break
        self.page = BeautifulSoup(requests.get(self.address).text, 'html.parser')
    def extractByField(self, field, map_to = None):
        index = fields[field]
        rows = self.page.findAll("tr", {"class":"rowleftcolumn"})
        observations = [row.findAll("td")[index].text for row in rows]
        if map_to:
            observations = list(map(map_to, observations))
        return observations
    def extractByFieldTime(self, field, datetime, map_to = None):
        extracted = self.extractByField(field, map_to)
        times = self.extractByField("Date/Time")
        return extracted[times.index(datetime)]
    def dailyFieldTime(self, field, time, outfile):
        while True:
            curr_date = extractByField("Date/Time")[0].split('/')[0]
            obs = extractByFieldTime(field, curr_date + time)
            saved = open(outfile, 'r').read()
            w = open(outfile, 'w')
            w.write('\n'+curr_date+'/'+time+','+obs)
            w.close()
            time.sleep(86400)
    def hourlyFieldTime(self, field, time, outfile):
        while True:
            curr_date = extractByField("Date/Time")[0].split('/')[0]
            obs = extractByFieldTime(field, curr_date + time)
            saved = open(outfile, 'r').read()
            w = open(outfile, 'w')
            w.write('\n'+curr_date+'/'+time+','+obs)
            w.close()
            time.sleep(3600)

if __name__ == "__main__":
    Region = input("Please enter Region: ")
    Area = input("Please enter Area: ")
    Location = input("Please enter Location: ")
    extract = ExtractBOM(Region, Area, Location)
    while True:
        prompt = input('>>> ')
        try:
            print(eval('extract.' + prompt))
        except:
            print("INVALID COMMAND")
