#1/usr/bin/env python3.7

import socket
import select

aws = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
aws.connect(('random-rpg.com', 8032))

self_ssh = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
aws.connect(('localhost', 22))

while True:
	readable, _, _ = select.select([aws, self_ssh], [], [])
	if aws in readable:
		self_ssh.send(aws.recv(1024))
	if self_ssh in readable:
		aws.send(self_ssh.recv(1024))
