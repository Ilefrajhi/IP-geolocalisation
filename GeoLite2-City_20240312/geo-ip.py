import geoip2.database

def get_geolocation(ip_address):
    try:
        # Load the GeoIP2 database
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')

        # Query the GeoIP2 database for the given IP address
        response = reader.city(ip_address)

        # Print the geolocation information
        print("Geolocation Information:")
        print(f"IP Address: {ip_address}")
        print(f"Country: {response.country.name}")
        print(f"Region: {response.subdivisions.most_specific.name if response.subdivisions else 'N/A'}")
        print(f"City: {response.city.name if response.city else 'N/A'}")
        print(f"Postal Code: {response.postal.code if response.postal else 'N/A'}")
        print(f"Latitude: {response.location.latitude}")
        print(f"Longitude: {response.location.longitude}")
        print(f"Time Zone: {response.location.time_zone if response.location.time_zone else 'N/A'}")
        print(f"Continent: {response.continent.name}")
        print(f"Metro Code: {response.location.metro_code if response.location.metro_code else 'N/A'}")

        # Close the GeoIP2 database reader
        reader.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    ip_address = input("Enter the IP address: ")
    get_geolocation(ip_address)

