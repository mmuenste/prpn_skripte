import json
import requests
from credentials import username, password, ip

URL = "http://{}/ins".format(ip)
CRED = (username, password)

COMMAND = {"ins_api": {"version": "1.0",
                       "type": "cli_show",
                       "chunk": "0",
                       "sid": "1",
                       "input": "sho vers",
                       "output_format": "json"
                       }}

HDR = {'Content-type': 'application/json',
       'Accept': 'application/json'}

RESP = requests.post(URL, headers=HDR, auth=CRED, data=json.dumps(COMMAND))

RESP_PAYLOAD = RESP.text

BODY = RESP.json()

with open('resp.json', 'w') as jsonfile:
    jsonfile.write(RESP.text)
PRC_BRD_ID = BODY['ins_api']['outputs']['output']['body']['proc_board_id']
print(PRC_BRD_ID)
