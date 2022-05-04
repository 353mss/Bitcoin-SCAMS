import code
from multiprocessing.connection import wait
import string
import random
from time import sleep
name = input("Enter Your BTC Address ")
print("Starting Up Miner")
sleep(1.5)
code = string.ascii_letters + string.digits
id = string.digits
for i in range(1000000):
   print ("[+] " + ''.join(random.choice(code) for i in range(32)) + " - [Gain: 0.00 BTC]")
print ("[+] " + ''.join(random.choice(code) for i in range(32)) + " - [Gain: 0.00886969 BTC]")
print ("BTC Deposited to " + name )
print ("Account Balance: 0.949284924 = $35966.22 USD")
sleep(0.8)
print ("Please Note this is fake!")
input("press any key to close")