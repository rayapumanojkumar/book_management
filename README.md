# How to setup this Project

1. Create a virtual environment and install dependencies using


      pip install -r requirements.txt

2. navigate to src directory in the repo
3. use the following command to run the project.


      uvicorn api:app --reload


4. create a .env file to setup your email, recipient-email and password


NOTE: "Since we don't have any specific user, we are hard-coding recipient email in .env file"
5. navigate to the following url to access api documentation.
