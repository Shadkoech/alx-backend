import { createClient, print } from 'redis';
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

// Function to display the value for a school in Redis
function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, value) => {
        if (error) {
            console.error(error);
            return;
        }
        console.log(value);
    });
};

// Calling the functions to display the output
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');