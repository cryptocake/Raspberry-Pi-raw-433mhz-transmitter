import sys
import wiringpi

OUTPUT = 1
TPIN = 17 # Use BCM GPIO pin number
RAW = str(sys.argv[1])
HIGH = False

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(TPIN,OUTPUT) # Set pin 17 to 1 ( OUTPUT )

print "Sending signal..."

for x in RAW.split():
    if HIGH:
        wiringpi.digitalWrite(TPIN, 0)
        HIGH = False
    else:
        wiringpi.digitalWrite(TPIN, 1)
        HIGH = True
    wiringpi.delayMicroseconds(int(x))

wiringpi.digitalWrite(TPIN, 0)
print "... sent!"
