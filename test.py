import subprocess

#this for loop depends on ho wlong you are willing to wait. I am
for i in range(255):
    command=['ping', '-n', '1','-w','100', '10.0.0.'+str(i)]
    subprocess.call(command)

arpa = subprocess.check_output(("arp", "-a")).decode("ascii")
n_devices=len([x for x in arpa.split('\n') if '10.0.0.' in x and  
    all(y not in x for y in ['10.0.0.1 ','10.0.0.255']) ])