import geoip2.database
import ipaddress

def track_ip(ip_address):
    # Specify the path to the GeoLite2 City database file
    database_path = '/usr/share/GeoIP/GeoLite2-City.mmdb'

    # Create a reader object to open the GeoLite2 database
    reader = geoip2.database.Reader(database_path)

    try:
        # Lookup the IP address
        response = reader.city(ip_address)

        # Retrieve the country and city from the response
        country = response.country.name
        city = response.city.name

        # Print the location information
        print(f"IP: {ip_address}")
        print(f"Country: {country}")
        print(f"City: {city}")

    except geoip2.errors.AddressNotFoundError:
        print("IP address not found in the database.")

    # Close the reader object
    reader.close()

# Get the IP address from user input
ip_address = input("Enter the IP address: ")

# Validate the IP address
try:
    ip = ipaddress.ip_address(ip_address)
except ValueError:
    print("Invalid IP address.")
else:
    # Track the IP address
    track_ip(ip_address)

