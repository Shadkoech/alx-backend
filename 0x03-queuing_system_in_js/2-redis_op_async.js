import { createClient, print } from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = createClient();

// Event listener in the instant that redis client connects succesfully
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Incase of failure of connection
client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error}`);
});

// Function to set a new school in Redis
function setNewSchool(schoolName, value) {
    client.set (schoolName, value, print);
}

// Promisify the get method of the Redis client
const getAsync = promisify(client.get).bind(client);

// Function to display the value for a school in Redis
async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value)
    } catch (error) {
        console.error(error);
    }
}

// Calling the functions to display the output
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');