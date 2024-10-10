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

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, data) => {
    console.log(data);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
