import http.client ,json

conn = http.client.HTTPSConnection("vgtechdemo.com")


def GetHotelCity(city):

    payload = f'{{\"search\": "{city}"}}'
    headers = {
        'Token': "gopaddi@v1",
        'Userid': "10"
        }

    conn.request("POST", "/gopaddiberlin/gopaddiberlinbkend/web/hotels/destinations", payload, headers)

    res = conn.getresponse()
    data = res.read()
    response=json.loads(data.decode("utf-8"))
    destination=response['data'][0]['destinations']
    hotellist=[]
    for i in destination:
        hotellist.append(i['title'])

    return hotellist


    #print(data.decode("utf-8"))