# s3-namegrabber
Continuously retries creating an AWS S3 bucket to grab the name as soon as it's available

Script uses `boto3` library to interface with AWS. Install via `pip3 install boto3`
Any time the status changes it will print the new message. Otherwise it will just increment the Attempt counter and Timestamp.

The delay between when a bucket has been deleted and the name becomes available has been reported to take from minutes to hours.


### Using the Docker image
To build docker image:
`docker build . -t s3-namegrabber --build-arg AWS_ACCESS_KEY=${AWS_ACCESS_KEY} --build-arg AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}`

To use the docker image:
`docker run -it s3-namegrabber <bucket-name>`
