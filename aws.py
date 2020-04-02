#!/usr/bin/env python3.7

import socket
import select

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 8030))
serversocket.listen(1)
desktop, _ = serversocket.accept()
serversocket.close()

usable_tcps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
usable_tcps.bind(('0.0.0.0', 8032))
usable_tcps.listen(10)

incoming_sshs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
incoming_sshs.bind(('0.0.0.0', 8031))
incoming_sshs.listen(10)

pending_sshs = list()
pairs = list()

while True:
	to_select = [item for pair in pairs for item in pair]
	to_select.append(usable_tcps)
	to_select.append(incoming_sshs)
	readable, _, _ = select.select(to_select, [], [])
	if incoming_sshs in readable:
		desktop.send('X')
		incoming_ssh, _ = incoming_sshs.accept()
		pending_sshs.append(incoming_ssh)

	if usable_tcps in readable:
		usable_tcp, _ = usable_tcps.accept()
		pairs.append((usable_tcp, pending_sshs.pop()))

	for pair in pairs:
		if pair[0] in readable:
			pair[1].send(pair[0].recv(1024))
		if pair[1] in readable:
			pair[0].send(pair[1].recv(1024))


