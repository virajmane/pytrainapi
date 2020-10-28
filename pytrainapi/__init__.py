import requests
from bs4 import BeautifulSoup
import json

class Train():
    def train_info(self, source, destination, date):
      base_url = f"https://www.railyatri.in/booking/trains-between-stations?from_code={source}+&to_code={destination}+&journey_date={date}"
      req = requests.get(base_url).text
      bs = BeautifulSoup(req, "html.parser")
      train_no = bs.find_all(class_="train_no_text")
      time_rating = bs.find_all(class_="on_time_text")
      rank = bs.find_all(class_="rank")
      dep_time = bs.find_all("p", class_="Departure-time Departure-time-text-1")
      src = bs.find_all(class_="Departure-time Departure-time-text-2")
      travel_time = bs.find_all(class_="TravelHour text-center")
      arr_time = bs.find_all(class_="Arrival-time Arrival-time-text-1 text-right")
      destination = bs.find_all(class_="Arrival-time Arrival-time-text-2")
      train_info = {}
      for i in range(len(train_no)):
          train_info[f"train_{i + 1}"] = {"on_time": time_rating[i].string, "train_name": bs.find(
              class_=f"TrainName Train_Name_{train_no[i].string}").string, "rank": rank[i].string.strip(),
                                          "departure_time": dep_time[i].text.strip(),
                                          "source": src[i].string.strip(),
                                          "travel_time": travel_time[i].string.strip(),
                                          "arrival_time": arr_time[i].text.strip(),
                                          "destination": destination[i].string.strip()}
      r = json.dumps(train_info)
      result = json.loads(r)
      return result

    def station_code(self, name):
      url = "https://indianrailways.p.rapidapi.com/findstations.php"
      querystring = {"station":name}
      headers = {
          'x-rapidapi-host': "indianrailways.p.rapidapi.com",
          'x-rapidapi-key': "8464831e75mshf2ffab92690de5fp19c898jsn2d20fcd6f536"
          }
      response = requests.request("GET", url, headers=headers, params=querystring).json()
      return response['stations']
