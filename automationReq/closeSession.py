import sessionController as s
import argparse
closeSessionPars = argparse.ArgumentParser()

#add ip address, this is mandatory
closeSessionPars.add_argument("ip", help= "<ipaddress>:<port>")

closeSessionPars.add_argument("-s","--session", type=str, help = "session id")

closeSessionArguments = closeSessionPars.parse_args()

def main():
    print(closeSessionArguments.session)
    return s.closeSession(closeSessionArguments.ip,closeSessionArguments.session)

main()