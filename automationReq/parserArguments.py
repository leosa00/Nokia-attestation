import argparse
#argparse for create element function
elementPars = argparse.ArgumentParser()
#add name of the device
elementPars.add_argument("-n", "--name", type=str,
                    help="element name")

#add description, this is optional, if this is not added the description will be generated automatically
elementPars.add_argument("-d", "--description", type= str, help="description of element")

#add ip address, this is mandatory
elementPars.add_argument("user", help= "<user>@<ip address>")

#tags such as tpm type, currently only supports one argument which is the tpm type
elementPars.add_argument("-t", "--tag", type = str, help="tag")

elementArguments = elementPars.parse_args()

#/////
#arparse for create expected value function

expectedPars = argparse.ArgumentParser()

expectedPars.add_argument("-n", "--name", type = str, help = "expected value name")

expectedPars.add_argument("-d", "--description", type = str, help = "description of expected value")

expectedPars.add_argument("-e", "--element", type = str, help = "element used for expected value")

expectedPars.add_argument("-p", "--policy", type = str, help = "policy used for expected value")

expectedArguments = expectedPars.parse_args()