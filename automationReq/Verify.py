import attestVerifyController as ver
import argparse

#creates an element
#argparse for create element function
verifyPars = argparse.ArgumentParser()


#tags such as tpm type, currently only supports one argument which is the tpm type
verifyPars.add_argument("-r", "--rule", type = str, help="rule name")

verifyPars.add_argument("-s", "--session", type = str, help="session id")

verifyPars.add_argument("-c", "--claim", type = str, help = "claim id")

verifyArguments = verifyPars.parse_args()

def main():
    rule = verifyArguments.rule
    sessionId = verifyArguments.session
    claimId = verifyArguments.claim
    
    
    return ver.sendRequest(claimId,sessionId,rule)

main()