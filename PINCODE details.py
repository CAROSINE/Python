from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")

zip_data = input("Enter the zipcode: ")
zipcode = zip_data

location =geolocator.geocode(zipcode)

print("Zipcode: ", zipcode)
print("Deatils  of the Zipcode: ")
print(location)