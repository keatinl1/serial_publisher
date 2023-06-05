# serial_publisher
### Read data from a serial port and publish it to a ROS2 node


If you don't have a serial device writing to a port, you can make a virtual one using these steps:

$~~~~~~~~~~$

1.

```socat -d -d pty,raw,echo=0 pty,raw,echo=0```


This will output two ports something like this (the numbers might be different for you):
```
2023/06/05 16:05:01 socat[30776] N PTY is /dev/pts/1
2023/06/05 16:05:01 socat[30776] N PTY is /dev/pts/5
2023/06/05 16:05:01 socat[30776] N starting data transfer loop with FDs [5,5] and [7,7]
```

$~~~~~~~~~~$

2.
Then using the output from that we'll write Test to one of the ports

```echo "Test" > /dev/pts/5```

$~~~~~~~~~~$

3.
The "Test" message can be read from the other port by our node
