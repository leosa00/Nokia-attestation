#checks to see if ek and ak exists on the device, if not then new keys are created
import os
import subprocess

def keycheck(device):
    try:
        keys = os.system(f"tpm2_getcap handles-persistent --tcti='cmd:ssh {device} tpm2_send'")
    except:
        raise Exception("key check failed, check the device username and ip address")
    print(keys)

#device variable gives the username and ip address of the device in the form <username>@<ipaddress>
#handles variable is a list of all the key handles that need to be deleted

def deleteKeys(device,handles):
    for key in handles:
        try:
            os.system(f"tpm2_evictcontrol -c {key} --tcti='cmd:ssh {device} tpm2_send'")
            os.system(f"tpm2_getcap handles-persistent --tcti='cmd:ssh {device} tpm2_send'")
        except:
            raise Exception("key deletion didnt work, check the device username, ip address and handle names")

#this function creates an EK and AK, requires parameter device given as <username>@<ipaddress>

def keyCreator(device):
    try:
        os.system(f"tpm2_createek -c 0x810100EE -G rsa -u ek.pub --tcti='cmd:ssh {device} tpm2_send'")
        os.system(f"tpm2_getcap handles-persistent --tcti='cmd:ssh {device} tpm2_send'")
        os.system(f"tpm2_createak -C 0x810100EE -c ak.ctx -G rsa -g sha256 -s rsassa -u ak.pub -f pem -n ak.name --tcti='cmd:ssh {device} tpm2_send'")
        os.system(f"tpm2_evictcontrol -c ak.ctx 0x810100AA --tcti='cmd:ssh {device} tpm2_send'")
    except:
        raise Exception("key creation didnt work, check the device username and ip address")
