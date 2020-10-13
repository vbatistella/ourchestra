import requests

#livestreamsecret: live_592589992_0Z7AKufUJ85C1MHz26R8EOvdSEenQa
#client secret: ysqmbbufnwkm7w7obp6l6ymtdcq28v

client_id = "ha7gnzycut10qrfhb2c0f0n3557wqm"
redirect_uri = "http://localhost"
response_type = "token"
scope = ""

url = 'https://id.twitch.tv/oauth2/authorize?client_id='+client_id+'&redirect_uri='+redirect_uri+'&response_type='+response_type+'&scope='+scope

#r = requests.get()

print(url)
