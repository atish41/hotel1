import http.client
import json

conn = http.client.HTTPSConnection("vgtechdemo.com")

def SearchHotelList1(city, rooms, nights,startDate, endDate, adults, children, ages):
#city="Bur Dubai, United Arab Emirates"
#rooms="1"
#nights="1"
#startDate="2024/04/07"
#endDate="2024/04/10"
#adults=1
#children=1
#ages=9
    payload = f"""{{
        "destination": "{city}",
        "rooms": "{rooms}",
        "nights": "{nights}",
        "dates": "{startDate} - {endDate}",
        "occupancy": [
            {{
                "room_no": 1,
                "adult": {adults},
                "child": {children},
                "child_age": [{ages}]
            }}
        ]
    }}"""


    headers = {
        'Token': "gopaddi@v1",
        'Userid': "10"
    }

    conn.request("POST", "/gopaddiberlin/gopaddiberlinbkend/web/hotels/search", payload, headers)

    res = conn.getresponse()
    data = res.read()
    response = json.loads(data.decode("utf-8"))
    hotels_list = response['data'][0]['hotelList']
    searchId=response['data'][0]['searchId']

    return searchId,hotels_list
