import * as net from 'net';

let client1 : net.Socket = null;
let client2 = null;

const server = net.createServer(socket => {
	let other = client2;
	if(client1) {
		client2 = socket;
		other = client1;
		console.log('second client connected.');
	} else {
		client1 = socket;
		other = client2;
		console.log('first client connected.');
	}
	socket.on('data', data => other.write(data));
});

server.listen(8090);
