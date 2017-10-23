#coding: utf-8
import requests,json


url = "https://webim-h5.easemob.com"
user1 = "auto01"
passwd1 = "1"
user2 = "auto02"
passwd2 = "1"
message = "this is test easemob"



tokenurl = "http://a1.easemob.com"
org = "easemob-demo"
app = "chatdemoui"
client_id = "YXA6TX5LoNxKEeOQ1eH_uqza9Q"
client_secret =  "YXA6DML6OxuXqwhjoetT7PX_eBQzg_M"

# get Admin token
def acquire_token(url,org,app,client_id,client_secret):
    tokenbody = {
        "grant_type": "client_credentials",
        "client_id": client_id ,
        "client_secret": client_secret
      }
    try:
        req = requests.post("%s/%s/%s/token" %(url,org,app),data=json.dumps(tokenbody),headers={'Content-Type': 'application/json'})
    except requests.exceptions.ConnectionError,e:
        return "Your url is error :", e.message
    try:
        if req.status_code == 200:
            contents = json.loads(req.content)
            tokens = contents["access_token"]
            expires_in = contents["expires_in"]
            return tokens,expires_in
        else:
            return req.status_code,req.content
    except UnboundLocalError,e:
        return e,e.message


token,expires_in = acquire_token(tokenurl,org,app,client_id,client_secret)

#print "Token is: %s, Expires_in is: %s" %(token,expires_in)
headers = {'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': "Bearer %s" % token}


def deluser(user):
    try:
        r = requests.delete("%s/%s/%s/users/%s" %(tokenurl,org,app,user), headers=headers)
        print r.content
    except:
        print "tokenurl is not exist"
