# SWE573_Software-Development-Practice_Fall22
This repository is created for the lecture SWE573, Software Development Practice.

## KeepItSocial

Keepitsocial is a social networking platform where users can connect with each other, share content, and engage with their community. With features like posting, liking, following, and joining spaces, Keepitsocial provides a dynamic and interactive experience for users to express themselves and explore new interests. Whether you're looking to share your thoughts, discover new content, or meet like-minded individuals, Keepitsocial has something for everyone.


## Deployment

To deploy the Keepitsocial platform on an EC2 Ubuntu server, follow these steps:


1. Set up a new EC2 instance using the Ubuntu AMI.
2. Connect to the instance using SSH.
3. Install Docker on the instance using the following command

`sudo apt-get update && sudo apt-get install docker.io`

4. Clone the Keepitsocial repository from GitHub using the following command:

`sudo git clone https://github.com/samedtorunn/SWE573_Software-Development-Practice_Fall22.git`

5. Navigate to the cloned repository using the cd command.
6. Build the Docker image using the following command

`docker build -t keepitsocial .`

7. Run the Docker container using the following command:

`docker run -p 8000:8000 keepitsocial`

8. Open a web browser and go to `http://[your_ec2_instance_public_ip]:8000` to access the Keepitsocial platform.

Note: You may need to add the EC2 instance's public IP to the ALLOWED_HOSTS list in the project's settings file. You may also need to run the Django migrations using the python manage.py migrate command before running the app.


## Authors

[Samed Torun](https://github.com/samedtorunn)

