import os

def copy_key_to_device(device):
    try:
        return os.system(f"ssh-copy-id -i ~/.ssh/id_rsa.pub {device}")
    except:
        raise Exception("copying ssh keys to device didnt work, please check the device username and ip address")
