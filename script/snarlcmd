#!/usr/bin/env python

import sys, os, socket

cmd = " ".join([((arg.find(" ") != -1) and ('"%s"' % arg) or arg) for arg in sys.argv[1:]])
print(cmd)
ret = os.spawnvp(os.P_WAIT, sys.argv[1], sys.argv[2:])

if len(cmd) > 100: cmd = cmd[:100] + " ..."

if ret < 0:
    prefix = "signal %d" % ret
elif ret == 0:
    prefix = "OK"
else:
    prefix = "ERROR %d" % ret

msg = "%s: %s" % (prefix, cmd)

print("sending message: %s" % msg)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.1', 10942))
s.send(("%s\r\n" % msg).encode())
s.close()
