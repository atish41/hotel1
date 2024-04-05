from hotelsearch1 import SearchHotelList1
from pprint import pprint
from hotelcity import GetHotelCity

#city=GetHotelCity("delhi")[0]
#print(city)
searchId,result = SearchHotelList1("Bur Dubai, United Arab Emirates","1","1","2024/04/07", "2024/04/08",1,1,9)
pprint(result)
print("this is the search id for hotel search",searchId)
#def SearchHotelList1(city, startDate, endDate, adults, children, ages, rooms, nights,room_No):
#city="Bur Dubai, United Arab Emirates"
#rooms="1"
#nights="1"
#startDate="2024/04/07"
#endDate="2024/04/10"
#adults=1
#children=1
#ages=9