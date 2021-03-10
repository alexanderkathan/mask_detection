# Mask Detection API

# Project Description
This project offers an API for mask detection during the corona virus. It is designed as an API service in order to enable other people to access this service from other computers for different applications. In order to start the service just run the mask_detection_api.py. Afterwards you can access the service directley over the following endpoint: http://{ip_of_your_server}:5000/ 
As a response you get a message that you can directly output to your customers. It contains a note about hygiene and safety regulation if it detects people without a mask and a thank-you-note if all people are wearing a mask.

# Design and related works
The original model for the mask detection was built and trained by balajisrinivas (https://github.com/balajisrinivas/Face-Mask-Detection). This previous work was extended by functions for the recognition of individual images and frames as well as the implementation of the API service.It is expanded All of the code is written in the programming language "Python". 
