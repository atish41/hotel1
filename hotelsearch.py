import http.client
import json

conn = http.client.HTTPSConnection("vgtechdemo.com")


def SearchHotelList(city,startDate,endDate,adults,Children,ages,rooms,nights):

    payload = f"""{{
        "destination":"{city}",
        "dates":"{startDate} - {endDate}",
        "adult":"{adults}",
        "child":"{Children}",
        "child_age":"{ages}",
        "rooms":"{rooms}",
        "nights":"{nights}"
        }}"""

    headers = {
        'Token': "gopaddi@v1",
        'Userid': "10"
        }

    conn.request("POST", "/gopaddiberlin/gopaddiberlinbkend/web/hotels/search", payload, headers)

    res = conn.getresponse()
    data = res.read()
    response=json.loads(data.decode("utf-8"))
    hotels_list=response['data'][0]['hotelList']
    
    return hotels_list

