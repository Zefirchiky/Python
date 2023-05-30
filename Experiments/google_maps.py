import csv
import googlemaps

# Replace 'YOUR_API_KEY' with your actual API key
gmaps = googlemaps.Client(key='AIzaSyBGhKU2eTEYxOFxRNksAaH0CLucC_EArc4')

# Geocode the region or city
geocode_result = gmaps.geocode('Region, Morocco')

# Open the CSV file for writing
with open('morocco_addresses.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')

    # Write the header row in the CSV file
    writer.writerow(['streetname', 'city', 'postcode', 'region', 'latitude', 'longitude'])

    # Iterate over the geocode results and extract relevant information
    for result in geocode_result:
        formatted_address = result['formatted_address']
        address_components = result['address_components']
        print(result)

        # Extract the required address details from the address components
        # You may need to adapt this part based on the structure of the geocode result
        streetname = ...
        city = ...
        postcode = ...
        region = ...
        latitude = ...
        longitude = ...

        # Write the extracted address data to the CSV file
        writer.writerow([streetname, city, postcode, region, latitude, longitude])

# Print a message when the CSV file generation is completed
print("CSV generation completed.")
