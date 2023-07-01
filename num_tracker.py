import requests

def track_number(phone_number):
    # Specify your NumVerify API access key
    api_key = "11edbf4bf2ea6d8fd4dcefe45b7994f1"

    # Send a GET request to the NumVerify API
    response = requests.get(f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}")

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Retrieve the location information from the response
        country = data['country_name']
        city = data['location']

        # Print the location information
        print(f"Phone Number: {phone_number}")
        print(f"Country: {country}")
        print(f"City: {city}")
    else:
        print("Failed to retrieve location information.")

# Get the phone number from user input
phone_number = input("Enter the phone number: ")

# Track the phone number
track_number(phone_number)

