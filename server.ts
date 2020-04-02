import * as net from 'net';
import * as process from 'process';

const client = net.createConnection(8090, process.argv[1]);
const ssh = net.createConnection(22);

client.on('data', data => ssh.write(data));
ssh.on('data', data => client.write(data));
