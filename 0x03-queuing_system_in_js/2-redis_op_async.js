import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to your server');
});

client.on('error', (err) => {
  console.error('error ${err.message} was encountered');
});

client.connect();

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

/** promisify the 'get' method **/
const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
