import { createQueue } from 'kue';

const queue = createQueue();


// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    // Track the progress of the job
    job.progress(0, 100);

    // Check if phoneNumber is blacklisted
    if (blacklistedNumbers.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    // Track the progress to 50%
    job.progress(0, 50);
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    return done();
  }
  
  //  Setting up a handler function for processing jobs in the queue
  queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});