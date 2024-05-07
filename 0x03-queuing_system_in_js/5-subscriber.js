import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Event listener in the instant that redis client connects succesfully
client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error}`);
});

// Subscribe to the "holberton school channel"
client.subscribe('holberton school channel');

// Event listener for messages received on sub channel
client.on('message', (channel, message) => {
    console.log(message);
    if (message == 'KILL_SERVER') {
        client.unsubscribe();
        client.quit();
    }
});
