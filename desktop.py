#!/usr/bin/env python3.7

import socket
import select
import asyncio

aws_persistent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
aws_persistent.connect(('random-rpg.com', 8030))

pairs = list()

while True:
	to_select = [item for pair in pairs for item in pair]
	to_select.append(aws_persistent)
	readable, _, _ = select.select(to_select, [], [])
	if aws_persistent in readable:
		_ = aws_persistent.recv(1)
		aws = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		aws.connect(('random-rpg.com', 8032))

		self_ssh = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self_ssh.connect(('localhost', 22))
		pairs.append((aws, self_ssh))
	
	for pair in pairs:
		if pair[0] in readable:
			pair[1].send(pair[0].recv(1024))
		if pair[1] in readable:
			pair[0].send(pair[1].recv(1024))
