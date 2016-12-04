# Raspberry-Pi-raw-433mhz-transmitter

A simple but effective 433mhz transmitter script. Use your raw timings, which you've captured with your e.g. Arduino, and replay by passing them through the script.

Install [WiringPi-Python](https://github.com/WiringPi/WiringPi-Python) and run the script.

```sh
$ sudo python rawTransmit.py "660 984 816 1420 1132 172 388 248 372 1484 2016 500 224 1632 576 56 1028 1504 316 2592 464 1580"
Sending signal...
... sent!
$ 
```

