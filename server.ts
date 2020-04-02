import * as net from 'net';
import * as process from 'process';

let ssh : net.Socket = null;

const client = net.createConnection(8090, 'random-rpg.com');
client.on('data', data => {
	if(ssh == null) {
		ssh = net.createConnection(22);
		ssh.on('data', data => client.write(data));
	}
	ssh.write(data);
});

