import requests
import attestController as att
import json


def createJson(claimId,sessionId,rule):
    dictionary = {
    "cid":claimId,
    "rule":rule,
    "sid":sessionId,
    "parameters":{}
    }
    return dictionary

def sendRequest(claimId,sessionId,rule):
    # Serializing json
    json_object = createJson(claimId,sessionId,rule)
    
    try:
        r = requests.post('http://194.157.71.11:8520/verify', json=json_object)
    except:
        raise Exception("request to verify was not successfull")
        
    response = r.json()
    if(response['result']==0):
        print(f"Verification for rule {rule} passed")
    else:
        print(f"Verification for rule {rule} failed")
    return r.json()