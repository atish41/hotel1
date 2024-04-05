from flask import Flask,request
from pprint import pprint
from hotelsearch1 import SearchHotelList1
app=Flask(__name__)

@app.route('/')
def demo():
    return 'this returns hotel search results'

def hotelhook():
    req=request.get_json(force=True)
    pprint(req)
    sessionInfo=req['sessionInfo']
    parameters=sessionInfo['parameters']
    destination=parameters['destination_city'] if parameters['destination_city'] else parameters['destination2']
    rooms=parameters['rooms']
    nights=parameters['nights']
    startDate=parameters['start-date']
    endDate=parameters['end-date']
    adults=parameters['adults']
    children=parameters['children']
    child_age=parameters['child_age']
    if (children!=0) and (child_age==''):
        for i in range(int(children)):
            child_age.append('7')
    total_people=int(adults)+int(children)


#def SearchHotelList1(city, rooms, nights,startDate, endDate, adults, children, ages):

    searchId,hotel_list=SearchHotelList1(destination,rooms,nights,startDate,endDate,adults,children,child_age)
    hotel_list=hotel_list[:7]
    response={
        "fulfillmentResponse":{
            "messages":[
                {
                    "text":{
                        "text":[
                            f"Click on above options to book!"
                        ]
                    }
                },
                {
                    "responseType":"RESPONSE_TYPE_UNSPECIFIED",
                    "channel":"",


                    #Union field message can be only one of the following:
                    "payload":{

                        "botcopy":[
                            {
                                "carousel":[
                                    {
                                        "action":{
                                            "message":{
                                                "type":"training",
                                                "command":"book now",
                                                "parameters":{
                                                    "searchId":f"\"{searchId}\"",
                                                    "hotelId":i["hotelId"],
                                                    "hotelName":i['hotelName'],
                                                    "hotelRating":i['hotelRating'],
                                                    "locality":i['locality'],
                                                    "nights":i['nights'],
                                                    "rooms":i['rooms'],
                                                    "totalPrice":i['totalPrice']
                                                }
                                            }
                                        },
                                        "body":f"{i['description'][:150]}....",
                                        "image":{
                                            "alt":"Image of Activity",
                                            "url":i['featureImage']
                                        },
                                        "subtitle":f"NGN {i['adultPrice']}",
                                        "title":i['hotelName']
                                    } for i in hotel_list
                                ]
                            }
                        ]
                    }

                }
            ]
        }
    }
    
    return response


if __name__=="__main__":
    app.run(debug=True,port=8060)
