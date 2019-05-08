import ipaddress
import random
import time
network = ipaddress.ip_network('192.168.1.0/24')
nexttime = time.time()

staticIPTV = ipaddress.ip_interface('192.168.1.20/24')
a=staticIPTV.ip
print('staticIPTV-->',a)
staticIPCAM = ipaddress.ip_interface('192.168.1.130/24')
b=staticIPCAM.ip
print('staticIPTV-->',b)
staticIPTAB = ipaddress.ip_interface('192.168.1.12/24')
c=staticIPTAB.ip
print('staticIPTAB-->',c)
def func():
    for x in range(0, 1):
        ipTV = "192.168.1."
        ipTV += ".".join(map(str, (random.randint(0, 255)
                                   for _ in range(1))))

        ipCAM = "192.168.1."
        ipCAM += ".".join(map(str, (random.randint(0, 255)
                                    for _ in range(1))))

        ipTAB = "192.168.1."
        ipTAB += ".".join(map(str, (random.randint(0, 255)
                                    for _ in range(1))))

        tv = ipaddress.ip_interface(ipTV)
        cam = ipaddress.ip_interface(ipCAM)
        tablet = ipaddress.ip_interface(ipTAB)
    a = tv.ip
    b = cam.ip
    c = tablet.ip
    print('tv ipaddress =', a)
    print('cam ipaddress =', b)
    print('tablet ipaddress =', c)
    nexttime = time.time()

while True:
    func()
    nexttime += 10
    sleeptime = nexttime - time.time()
    if sleeptime > 0:
        time.sleep(sleeptime)

