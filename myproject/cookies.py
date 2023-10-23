import json

# Your JSON data
json_data = [
    {
        "domain": ".google.fr",
        "expirationDate": 1713604360.645163,
        "hostOnly": False,
        "httpOnly": True,
        "name": "AEC",
        "path": "/",
        "sameSite": "lax",
        "secure": True,
        "session": False,
        "storeId": "1",
        "value": "Ackid1T-gZp8f6h0NwQq03I_wpv6bQN2xr5d_8ArYiV2mG7cCZscafdD0w",
        "id": 1
    },
    {
        "domain": ".google.fr",
        "expirationDate": 1713604360.645223,
        "hostOnly": False,
        "httpOnly": False,
        "name": "CONSENT",
        "path": "/",
        "sameSite": "unspecified",
        "secure": True,
        "session": False,
        "storeId": "1",
        "value": "PENDING+725",
        "id": 2
    },
    {
        "domain": ".google.fr",
        "expirationDate": 1713604362.593171,
        "hostOnly": False,
        "httpOnly": True,
        "name": "NID",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "1",
        "value": "511=bsJpf5cJ0CdDAH2QmxnvGX2PCCIzrCtflJ3bIMSd8cEdTp4AccPrYJFV5uiiGaLRU9UwvRsnjeEtOeQ9LevknvK3tzwXh8FjJ71U2rClbY5hXQSU_kHXrClwdLhxCNARTfmedZaC1FtD7RWQ8OI7E9nQEtwsEAcNJiJ311C57ws",
        "id": 3
    },
    {
        "domain": ".google.fr",
        "expirationDate": 1713604362.593124,
        "hostOnly": False,
        "httpOnly": False,
        "name": "SOCS",
        "path": "/",
        "sameSite": "lax",
        "secure": True,
        "session": False,
        "storeId": "1",
        "value": "CAISNQgEEitib3FfaWRlbnRpdHlmcm9udGVuZHVpc2VydmVyXzIwMjMxMDE3LjA0X3AwGgJmciACGgYIgO_WqQY",
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
