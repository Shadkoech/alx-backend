import { createClient } from 'redis';
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
