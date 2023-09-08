import attestController as att
import expectedValueController as e
import argparse

attestPars = argparse.ArgumentParser()
#add name of the device
attestPars.add_argument("-e", "--element", type=str,
                    help="element name")

#add description, this is optional, if this is not added the description will be generated automatically
attestPars.add_argument("-p", "--policy", type= str, help="policy name")

#tags such as tpm type, currently only supports one argument which is the tpm type
attestPars.add_argument("-s", "--session", type = str, help="session id")


attestArguments = attestPars.parse_args()

#creates an attest claim
def attest():
    elementId = e.element_id_finder(attestArguments.element)
    policyId = e.policy_id_finder(attestArguments.policy)
    return att.sendRequest(elementId, policyId, attestArguments.session, {
      "param1": "value1",
      "param2": "",
      "param3": ""
    })
    
attest()
