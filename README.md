# serial_publisher
read data from a serial port and publish it to a ros2 node


Publish data to a virtual serial port using socat

```socat -d -d pty,raw,echo=0 pty,raw,echo=0```

Then using the outpur from that

```echo "Test" > /dev/pts/5```
