
from folium import Map
from geo import Geopoint 

# get input values  
latitude = 40.09
longitude = float("3.74")
 
antipode_latitude = latitude * -1
# add 180 for negitive subtrack 180 for postive
if longitude <= 0.0:
    antipode_longitude = longitude + 180
else:
    antipode_longitude = longitude -180

loctaion = [antipode_latitude, antipode_longitude]

mymap = Map(loctaion)
mymap.save("antipode.html")

mypoint = Geopoint(41.2, 4.1)
mypoint.closest_parallel()
print(mypoint.closest_parallel())

# printing out varibles 
print(antipode_latitude)
print(antipode_longitude)
print(mymap)