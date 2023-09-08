#!/bin/bash
server="194.157.71.11:8520"
policy1="Pi Fakeboot CRTM"
policy2="Pi Fakeboot SRTM"
rule1="tpm2_attestedValue"
rule2="tpm2_firmware"

session=$(python3 createSession.py $server -m "bash script test")
echo "session $session opened"

while read -r name device; do
    python3 createElement.py $device -d "$name element" -n $name -t "letstrust"
    claim1=$(python3 Attest.py -e $name -p "$policy1" -s $session)
    claim2=$(python3 Attest.py -e $name -p "$policy2" -s $session)
    python3 createExpected.py -n "expected value for $name" -d "expected value for policy $policy1" -e "$name" -p "$policy1" -s $session -c $claim1
    python3 createExpected.py -n "expected value for $name" -d "expected value for policy $policy2" -e "$name" -p "$policy2" -s $session -c $claim2
done < elements.txt


while read -r name device; do
    claim1=$(python3 Attest.py -e $name -p "$policy1" -s $session)
    claim2=$(python3 Attest.py -e $name -p "$policy2" -s $session)
    python3 Verify.py -r "$rule1" -s $session -c $claim1
    python3 Verify.py -r "$rule2" -s $session -c $claim1
    python3 Verify.py -r "$rule1" -s $session -c $claim2
    python3 Verify.py -r "$rule2" -s $session -c $claim2
done < elements.txt


python3 closeSession.py $server -s $session
echo "session $session closed"