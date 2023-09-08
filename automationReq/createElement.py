#!/usr/bin/python3
import elementController as el
import sshKey as sshkey
import argparse

#creates an element
#argparse for create element function
elementPars = argparse.ArgumentParser()
#add name of the device
elementPars.add_argument("-n", "--name", type=str,
                    help="element name")

#add description, this is optional, if this is not added the description will be generated automatically
elementPars.add_argument("-d", "--description", type= str, help="description of element")

#add ip address, this is mandatory
elementPars.add_argument("device", help= "<user>@<ip address>")

#tags such as tpm type, currently only supports one argument which is the tpm type
elementPars.add_argument("-t", "--tag", type = str, help="tag")

elementArguments = elementPars.parse_args()

def main():
    #sshkey.copy_key_to_device(ipaddr)
    el.ekExtract(elementArguments.device)
    el.akExtract(elementArguments.device)
    ipaddr = elementArguments.device.split("@",1)[1]
    akInfo = "ak.txt"
    ekInfo = "ek.txt"
    ak= el.extract_name_and_public_key(akInfo)
    ek= el.extract_name_and_public_key(ekInfo)
    el.sendRequest(elementArguments.name,elementArguments.description,f"http://{ipaddr}:8530",elementArguments.tag,ek,ak)
    

main()