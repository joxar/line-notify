import requests
import sys
import urlparse

TOKEN = 'JVU6OPrXs78N5Fl5m9Py7U70VkmDttmbShTpenlDaoF'
API_ENTRYPOINT = 'https://notify-api.line.me/api/notify'

post_data = {'message': sys.argv[1], 'stickerPackageId': 1, 'stickerId': 2}
headers = {'Authorization': 'Bearer ' + TOKEN}
res = requests.post(API_ENTRYPOINT, data=post_data, headers=headers)

print(res.text)
