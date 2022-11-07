import requests
import json
import pandas as pd

def tautulli_user_stats(rating_key):
    tautulli_api = '0f0d4471a13e4c4283e619fc2118beff'
    tautulli_url = 'https://tautulli.notgeorge.duckdns.org/api/v2/?apikey=' + tautulli_api + '&cmd=' + 'get_item_user_stats' + '&rating_key=' + rating_key
    tautulli = requests.get(tautulli_url)
    return tautulli.json()

overseerr_api = 'MTY0NTQxMjkxMzA5NDVkMjBiZTk4LWU1YjctNGIwNC04M2U5LThmYTY2OWM5NjgwNyk='
overseerr_request_url = 'https://overseerr.notgeorge.duckdns.org/api/v1/request?filter=available&take=10000'
overseer_headers = {'X-Api-Key': overseerr_api}
overseerr = requests.get(overseerr_request_url,headers = overseer_headers)

item_request = overseerr.json()
overseerr_ratingKey = []
overseerr_user = []
overseerr_added = []
for i in item_request['results']:
    ratingKey = i['media']['ratingKey']
    user = i['requestedBy']['plexUsername']
    media_added = i['media']['mediaAddedAt']
    overseerr_ratingKey.append(ratingKey)
    overseerr_user.append(user)
    overseerr_added.append(media_added)

df = pd.DataFrame()
df['ratingKey'] = overseerr_ratingKey
df['user'] = overseerr_user
df['added'] = overseerr_added

#print(tautulli_user_stats('7280'))

#print(df)

for key, value in df['ratingKey'].iteritems():
    ratingKey = value
    print(ratingKey)
    print(tautulli_user_stats(str(ratingKey)))