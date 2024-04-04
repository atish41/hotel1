from flask import Flask,request
from pprint import pprint
from hotelcity import GetHotelCity


app=Flask(__name__)

@app.route('/')
def add():
    return "this is webhook for hotel search"

@app.route('/hotel')
def add1():
    return "this is webhook for hotel search and what are you looking for!"

@app.route('/hotel',methods=['POST'])
def hook():
    req=request.get_json(force=True)
    sessionInfo=req['sessionInfo']
    destination_city=req['sessionInfo']['parameters']['destination_city']
    session_name=req.get('sessionInfo').get('session')
    destination_list=GetHotelCity(destination_city)

    if not destination_list:
        no_destination={
            "fulfillment_response":
            {
                "messages":[
                    {
                        "text":{
                            "text":[
                                f"Sorry, we couldn't find any destinations in {destination_city}, Please try another city."
                            ]
                        }
                    }
                ]
            },
            "session_Info":{
                "session":session_name,
                "parameters":{
                    "destination_city":None
                }
            },
            "target_page":req.get('pageInfo').get('currentPage') #maintain current page
        }

        return no_destination
    
    elif len(destination_list)>1:
        manydestination={
            "fulfillment_response":
            {
                "messages":[
                    {
                        "responseType":"RESPONS_ETYPE_UNSPECIFIED",
                        "channel":"",

                        #field messages can be one of the following
                        "text":{
                            "text":[
                                f'we have found multiple destination name with{destination_city} in it'
                                ],
                                    "allowPlaybackInterruption":False
                        }

                    },
                    {
                        "responseType":"RESPONSE_TYPE_UNSPECIFIED",
                        "channel":"",

                        #union field msg can be from one of them
                        "payload":{

                        "botcopy":[
                            {
                                "suggestions":[
                                    {
                                        "action":{
                                            "message":{
                                                "command":i,
                                                "type":"training"
                                            }
                                        },
                                        "title":i
                                    }for i in destination_list
                                ]
                            }
                        ]
                        }
                    }

                ],
                "mergeBehavior":"REPLACE"
            },
        
            "session_info":{
                "session":session_name,
                "parameters":{
                    "destination_city":None
                }

            },
            
        "target_page":"projects/travel-chatbot-409605/locations/us-central1/agents/ad7caede-bce6-4562-ae2f-8dacfb73bddf/flows/3ed31d48-076e-4f40-a75b-50f8dd046c81/pages/cac25836-ebea-49a0-adca-8bfd687fa215"
        

        }

        return manydestination
    else:
          perfect={


            "session_info":{
                "session":session_name,
                "parameters":{
                    "destination_city":destination_list[0]
                }

            
            },
                "target_page":"projects/travel-chatbot-409605/locations/us-central1/agents/ad7caede-bce6-4562-ae2f-8dacfb73bddf/flows/3ed31d48-076e-4f40-a75b-50f8dd046c81/pages/68e3c15c-ccc1-4593-a687-07d7f3955843"


        }
          

    return perfect

          

if __name__=="__main__":
    app.run(debug=True,port=4000)


