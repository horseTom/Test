import requests

def get_access_token():
    CORP_ID = 'ww75c9f5214ba2cb9b'
    Punch_CORP_SECRET = 'zX6o1r32YQicaXPgFgPg3e_p0HGE5YicIbi5GLxwQpY'
    URL = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?'
    HEADER = {'Accept': 'application/json'}
    data = {'corpid':CORP_ID, 'corpsecret':Punch_CORP_SECRET}

    res = requests.get(url=URL, headers=HEADER, params=data).json()
    if res['errcode'] == 0 :
        print("Access_Token: " + res['access_token'])
    else:
        print("error")

if __name__ == '__main__':
    get_access_token()