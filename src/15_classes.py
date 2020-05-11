# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
  def __init__(self, lat, lon):
   self.lat = lat
   self.lon = lon

place1 = LatLon(30.7162, 45.0298)

print("Lat: ",place1.lat)
print("Lon: ",place1.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

print(place1) ##<__main__.LatLon object at 0x009B8148>
print(place1.__doc__)

## Note - (source:https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods)
## The reason we use super is so that child classes that may be 
# using cooperative multiple inheritance will call the 
# correct next parent class function in the Method 
# Resolution Order (MRO).

# class ChildB(Base):
#     def __init__(self):
#         super().__init__() 

# YOUR CODE HERE



# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
## print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
## print(geocache)
