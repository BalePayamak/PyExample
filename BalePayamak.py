#Import needed Library
from requests import get

# Define Variables
url = "https://balesms.ir/v1/sendsms"
Number = "093000000"
apiKEY = "xxxxxxxxxxxxxxxxxxx"
template = "xxxxxxxxx"
Value = "1542"

data = {
    "api_key": apiKEY,
    "phone": Number,
    "template": template,
    "value": Value
    }

# Send Request
get(url, data=data)
