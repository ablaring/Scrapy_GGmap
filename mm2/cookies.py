import json

# Your JSON data
json_data = [
    {
        "domain": ".google.fr",
        "expirationDate": 1712414514.030686,
        "hostOnly": False,
        "httpOnly": True,
        "name": "AEC",
        "path": "/",
        "sameSite": "lax",
        "secure": True,
        "session": False,
        "storeId": "1",
        "value": "Ackid1RWtwLUgbohNkyzLZ7_X-X6HHxIg3lylE9iTMDtYBnoQrb73T2Mlw",
        "id": 1
    },
    {
        "domain": ".google.fr",
        "expirationDate": 1712414514.030739,
        "hostOnly": False,
        "httpOnly": False,
        "name": "CONSENT",
        "path": "/",
        "sameSite": "unspecified",
        "secure": True,
        "session": False,
        "storeId": "1",
        "value": "PENDING+318",
        "id": 2
    },
    {
        "domain": ".google.fr",
        "expirationDate": 1712414516.422762,
        "hostOnly": False,
        "httpOnly": True,
        "name": "NID",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "1",
        "value": "511=poW9EyFCl_-wizpGSzReWtIGK8QyTDrK4Y1sqPmK3ELySn47rwziwAH5xVWpy8rzgL45xJ0BuPXHTozqTZQLovUlcnIC8-6t6RLD53tFUNMvk9nwVsPVDaEtz03o9w0e4CP8Vwh5BQOeYOfRq8HQp2T8v6j3m8NCVLf_x8Ua9hc",
        "id": 3
    },
    {
        "domain": ".google.fr",
        "expirationDate": 1712414516.42272,
        "hostOnly": False,
        "httpOnly": False,
        "name": "SOCS",
        "path": "/",
        "sameSite": "lax",
        "secure": True,
        "session": False,
        "storeId": "1",
        "value": "CAISNQgEEitib3FfaWRlbnRpdHlmcm9udGVuZHVpc2VydmVyXzIwMjMxMDAzLjA2X3AwGgJmciACGgYIgIWNqQY",
        "id": 4
    }
]

# Convert JSON data to the desired dictionary format
cookies_dict = {item['name']: item['value'] for item in json_data}

# Format the dictionary as a string
cookies_str = f"cookies = {json.dumps(cookies_dict, indent=4)}"

# Write the formatted string to a text file
with open('cookies.txt', 'w') as file:
    file.write(cookies_str)
