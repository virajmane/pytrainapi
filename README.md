
<h1>PyTrainAPI</h1>

Gives you information about trains from source to destination and station code
<br>
<br>
<b>Code Snippet</b>
```
from pytrainapi import Train

t = Train()
print(t.train_info("pune","sur","29 oct"))
print(t.station_code("solapur"))
```


<b>Sample Output</b>
```
{'train_1': {'on_time': '10', 'train_name': '01139  MUMBAI CSMT - GADAG Covid Special', 'rank': '6', 'departure_time': '01:00 PUNE', 'source': 'PUNE JN', 'travel_time': '4 H 10 M', 'arrival_time': '05:10  SUR', 'destination': 'SOLAPUR JN'}, 'train_2': {'on_time': '10', 'train_name': '02701  MUMBAI CSMT - HYDERABAD Hussain Sagar Covid Special', 'rank': '6', 'departure_time': '01:15 PUNE', 'source': 'PUNE JN', 'travel_time': '4 H 15 M', 'arrival_time': '05:30  SUR', 'destination': 'SOLAPUR JN'}, 'train_3': {'on_time': '3', 'train_name': '06588  BIKANER - YESVANTPUR Covid Special', 'rank': '6', 'departure_time': '02:09 PUNE', 'source': 'PUNE JN', 'travel_time': '6 H 26 M', 'arrival_time': '08:35  SUR', 'destination': 'SOLAPUR JN'}, 'train_4': {'on_time': '3', 'train_name': '02115  MUMBAI CSMT - SOLAPUR Siddheshwar Covid SF Special', 'rank': '6', 'departure_time': '02:20 PUNE', 'source': 'PUNE JN', 'travel_time': '4 H 30 M', 'arrival_time': '06:50  SUR', 'destination': 'SOLAPUR JN'}, 'train_5': {'on_time': '7', 'train_name': '01301  MUMBAI CSMT - KSR BENGALURU Udyan Covid Special', 'rank': '6', 'departure_time': '11:35 PUNE', 'source': 'PUNE JN', 'travel_time': '4 H 25 M', 'arrival_time': '16:00  SUR', 'destination': 'SOLAPUR JN'}, 'train_6': {'on_time': '9', 'train_name': '01019  MUMBAI CSMT - BHUBANESWAR Konark Covid Special', 'rank': '6', 'departure_time': '18:55 PUNE', 'source': 'PUNE JN', 'travel_time': '5 H 15 M', 'arrival_time': '00:10  SUR', 'destination': 'SOLAPUR JN'}, 'train_7': {'on_time': '-1', 'train_name': '07017  RAJKOT - SECUNDERABAD Festival Special', 'rank': '6', 'departure_time': '22:30 PUNE', 'source': 'PUNE JN', 'travel_time': '4 H 25 M', 'arrival_time': '02:55  SUR', 'destination': 'SOLAPUR JN'}, 'train_8': {'on_time': '-1', 'train_name': '04806  BARMER - YESVANTPUR Covid AC Special', 'rank': '6', 'departure_time': '02:00 PUNE', 'source': 'PUNE JN', 'travel_time': '6 H 35 M', 'arrival_time': '08:35  SUR', 'destination': 'SOLAPUR JN'}}
[{'stationName': 'SOLAPUR JN', 'stationCode': 'SUR'}]
```

<b>Installation</b> <br>
```pip install pytrainapi==2.1``` <br>
https://pypi.org/project/pytrainapi/2.1/
