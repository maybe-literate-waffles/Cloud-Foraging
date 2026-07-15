# Cloud-Foraging
Hello! 
I'm teaching myself python, and instead of following a tutorial I decided to jump straight into a project.
So Cloud-Foraging is my **first ever** python script :D

My other goal with this project is to produce a dataset of my own for my next project! Because this puts all the generated data into a database I can use **that** database for my next project. Nifty isn't it? :P 

### What it does:
Its pretty simple -- A python script that fetches weather data from an API, cleans it up and stores it in a database!

### Stack
- Python
- Jupyter Notebook
- PostgreSQL
- psycopg3

And I used **Open Meteo** for the API.

### How to Run It & See It In Action
Oh also! If you want to run my little creation, you just need Python and the requests library (for now):

~~~ bash
pip install requests
pip install "psycopg[binary]"
python main.py
~~~
What you'll see in the terminal:

Plaintext
~~~
[26.1, '°C', 40.8, 140.75, 'GMT+9', '01:11:21']
~~~
(Note: It runs forever until you hit Ctrl + C to stop it. That's by design for now!)
