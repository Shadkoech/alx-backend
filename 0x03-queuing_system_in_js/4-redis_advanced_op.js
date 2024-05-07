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


// Creating hash in Redis
client.hset('HolbertonSchools', 'Portland', '50', print);
client.hset('HolbertonSchools', 'Seattle', '80', print);
client.hset('HolbertonSchools', 'New York', '20', print);
client.hset('HolbertonSchools', 'Bogota', '20', print);
client.hset('HolbertonSchools', 'Cali', '40', print);
client.hset('HolbertonSchools', 'Paris', '2', print);

//Display the hash stored in Redis
client.hgetall('HolbertonSchools', (error, result) => {
    if (error) {
        console.log(error);
        throw error;
    }
    console.log(result);
});
