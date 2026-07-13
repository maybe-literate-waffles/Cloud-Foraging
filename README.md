# Cloud-Foraging
Hello! 
I'm teaching myself python, and instead of following a tutorial I decided to jump straight into a project.
So Cloud-Foraging is my **first ever** python script :D

My other goal with this project is to produce a dataset of my own for my next project! Because this puts all the generated data into a database I can use **that** database for my next project. Nifty isn't it? :P 

### What it does:
Its pretty simple -- A python script that fetches weather data from an API, cleans it up and stores it in a database!

### Stack (so far)
- Python
- Jupyter Notebook

And I used **Open Meteo** for the API.

### How to Run It & See It In Action
Oh also! If you want to run my little creation, you just need Python and the requests library (for now):

~~~ bash
pip install requests
python main.py
~~~
What you'll see in the terminal:

Plaintext
~~~
{'temperature': 21.5, 'unit': '°C', 'latitude': 40.82, 'longitude': 140.74, 'timezone': 'JST'} and time: 22:24:05
~~~
(Note: It runs forever until you hit Ctrl + C to stop it. That's by design for now!)
