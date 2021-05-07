# import map from folium
from folium import Map

# get input values  
latitude = float("40.09")
longitude = float("3.74")

antipode_latitude = latitude.__mul__(int("-1"))
# add 180 for negitive sub 180 for postive
if longitude.__lt__(float("0")):
    antipode_longitude = longitude.__add__(float("180"))
elif longitude.__eq__(float("0")):
    antipode_longitude = float("1800")
elif longitude.__gt__(float("180")):
    antipode_longitude = str("Invalid Longitude")
else:
    antipode_longitude = longitude.__sub__(float("180"))

loctaion = list((antipode_latitude, antipode_longitude))
mymap = Map(loctaion)
mymap.save(str("antipode.html"))

# printing out varibles 
print(antipode_latitude)
print(antipode_longitude)
print(mymap)

 
