import { createQueue } from 'kue';

// create an instance of queue
const queue = createQueue();

// Creat a job object
const jobData = {
    phoneNumber: '+254727221023',
    message: 'This is the code to verify your account',
};

// Create a job and add it to the queue
const job = queue.create('push_notification_code', jobData).save((error)=>{
    if(error){
        return
    } else{
        console.log(`Notification job created: ${job.id}`);
    }
});

// When job is completed
job.on('complete', ()=>{
    console.log('Notification job completed');
});

// When job fails
job.on('failed', ()=>{
    console.log('Notification job failed');
});
