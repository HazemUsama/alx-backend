import { createClient } from 'redis';

const client = await createClient()
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', err => {
    console.log(`Redis client not connected to the server: ${err}`)
  });


await client.set('Hazem', 'Zo');
client.get('Holberton', (_, data) => {
  console.log(data);
});
