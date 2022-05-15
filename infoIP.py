import requests

headers = { "authority" : "infoip.io",
"method" : "GET",
"path" : "/",
"scheme" : "https",
"accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding" : "gzip, deflate, br",
"accept-language" : "es-ES,es;q=0.9",
"cache-control" : "max-age=0",
"client-ip" : "91.208.2.126",
"dnt" : "1",
"if-modified-since" : "Wed, 05 Feb 2020 00:02:36 GMT",
"if-none-match" : '"30028d266b4ad4d662165dced30c1ab42fa7f231529c4a83cb26e2a9a6ef7281"',
"sec-fetch-dest" : "document",
"sec-fetch-mode" : "navigate",
"sec-fetch-site" : "none",
"sec-fetch-user" : "?1",
"sec-gpc" : "1",
"upgrade-insecure-requests" : "1",
"user-agent" : "Mozilla/5.0 (Windows NT 10.0; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.82 Safari/537.36 Vivaldi/2.3.1440.41",
"via" : "Proxy",
"x-forwarded-for" : "91.208.2.126" }

content = requests.get("https://api.infoip.io/", headers=headers)
info = content.json()
print(
f"""
Tu IP es: {info['ip']}
Tu país es: {info['country_long']}
Tu ciudad es: {info['city']}, {info['region']}
Tu CP es: {info['postal_code']}
Timezone: {info['timezone']}
Lat/Long: {info['latitude']}/{info['longitude']}
"""
)