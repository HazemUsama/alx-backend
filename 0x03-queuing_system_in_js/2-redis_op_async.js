import { promisify } from 'util';
import { createClient, print } from 'redis';

const client = await createClient()
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', err => {
    console.log(`Redis client not connected to the server: ${err}`)
  });

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const get = promisify(client.get).bind(client);
  const value = await get(schoolName);
  console.log(value);
}

await displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');
