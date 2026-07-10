<p>SO this project is named Sentiment Predicition api using fast api to analyze the tweets for positive,negative, or neutral sentiment using natural language processing (NLP).
Prerequisites
• Python 3.8 or higher
• VS Code 
• Windows operating system</p>

create an app.py file under your sentiment analysis project and initialize a virtual environemnt using the commnad **python -m venv venv** creating a virtual environment help as without the virtual environment all the files would use the same packages that are isntalled therefore by creatig a virtual environment we can isolate the use of packages to specific files.
Activate the environment using **venv/Script/ACtivate**
now to install package run this command on terminal **pip install fastapi uvicorn textbob pandas**
verify using **pip list**
Then copy the code in the app.py and paste it into the vs code(app.py)
Run the code 
run this on terminal **uvicorn app:app --reload**
you would see a link like https://127.0.0.1:8000/docs
click on it and it will take you to a web browser and there click on try it out and then paste of tweets in json format.
