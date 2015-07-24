import json
from googleplaces import GooglePlaces, types, lang

API_KEY='AIzaSyD4yhh4YrL8gwTHp_Ktpylr30H-VTw8gr8'

google_places = GooglePlaces(API_KEY)

query_result = google_places.nearby_search(location='Guntur', keyword='Apartments',radius=20000)

#for place in query_result.places:
    # Returned places from a query are place summaries.
   # print place.name
   # print place.geo_location
   # print place.place_id

place=query_result.places[0]
place.get_details()
#data = json.load(details)
#print data
print place.details
#f=open('info.txt','w')
#f.write(place.details)
#f.close()



