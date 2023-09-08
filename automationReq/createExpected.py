import expectedValueController as ex
import argparse

#arparse for create expected value function

expectedPars = argparse.ArgumentParser()

expectedPars.add_argument("-n", "--name", type = str, help = "expected value name")

expectedPars.add_argument("-d", "--description", type = str, help = "description of expected value")

expectedPars.add_argument("-e", "--element", type = str, help = "element used for expected value")

expectedPars.add_argument("-p", "--policy", type = str, help = "policy used for expected value")

expectedPars.add_argument("-c", "--claim", type = str, help = "claim id")

expectedPars.add_argument("-s", "--session", type = str, help = "session id")

expectedArguments = expectedPars.parse_args()


#creates an expected value
def main():
    
    name = expectedArguments.name
    desc = expectedArguments.description
    element = expectedArguments.element
    policy = expectedArguments.policy
    sessionId = expectedArguments.session
    claimId = expectedArguments.claim
  
    policyId = ex.policy_id_finder(policy)
    elementId = ex.element_id_finder(element)
    intent = ex.check_policy_intent(policyId)

    if (intent != "tpm2/quote"):
      raise Exception(f"policy {policy} cannot be used to create an expected value, needs to have tpm2/quote intent") 


    pcrdigest,firmwareVersion = ex.getEVs(claimId)
    evs = {
      "attestedValue":pcrdigest,
      "firmwareVersion":str(firmwareVersion)
    }

    return ex.sendRequest(name,desc,elementId,policyId,evs)


main()