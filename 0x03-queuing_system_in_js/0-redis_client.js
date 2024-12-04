import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to your server');
});

client.on('error', (err) => {
  console.error('error ${err.message} was encountered');
});

client.connect();
