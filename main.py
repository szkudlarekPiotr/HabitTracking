import requests
from datetime import date, timedelta
import os

now = date.today()
today = str(now.strftime("%Y%m%d"))

#       Creating user

user_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":os.environ['PIXELA_TOKEN'],
    "username":"piotrszkud",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

auth_headers = {
    "X-USER-TOKEN":user_params['token']
}

graphid = "graph1"

# response = requests.post(url=endpoint, json=user_params)
# print(response)


#        Creating graph

# endpoint = f"{user_endpoint}/{user_params['username']}/graphs"

# graph_params = {
#     "id":"graph1",
#     "name":"Cycled kilometers",
#     "unit":"km",
#     "type":"float",
#     "color":"momiji"
# }


# response = requests.post(url=endpoint, headers=graph_headers, json=graph_params)
# print(response.text)


#       Adding data to graph

# endpoint = f"{user_endpoint}/{user_params['username']}/graphs/{graphid}"


# parameters = {
#     "date":today,
#     "quantity":"10.9"
# }

# response = requests.post(url=endpoint, headers=auth_headers, json=parameters)
# print(response.text)


#        Update data

# endpoint = (f"{user_endpoint}/{userparams['username']}/graphs"
#             f"/{graphid}/{today}")

# update_json = {
#     "quantity":"0.5",
# }

# response = requests.put(url=endpoint, headers=auth_headers, json=update_json)
# print(response.text)


#       Delete data

endpoint = (f"{user_endpoint}/{user_params['username']}/graphs"
            f"/{graphid}/{today}")

response = requests.delete(url=endpoint, headers=auth_headers)
print(response.text)
