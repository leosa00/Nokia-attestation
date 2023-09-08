import os
import keysController as k
import sshKey as s
import argparse
import sshKey as key
#arparse for creating keys

keyPars = argparse.ArgumentParser()

keyPars.add_argument("device", help = "<username>@<ip address>")

keyArguments = keyPars.parse_args()


def main():
    try:
        #s.copy_key_to_device(device)
        key.copy_key_to_device(keyArguments.device)
        k.deleteKeys(keyArguments.device,["0x810100AA","0x810100EE"])
        k.keyCreator(keyArguments.device)
        return k.keycheck(keyArguments.device)
    except:
        raise Exception("key creation didnt work")
main()