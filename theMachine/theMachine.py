#creating objects of a class

#from resources.classes.Person import Person
#print("hello world")
#philo = Person("Philo", 5)
#ikey = Person("Mikey", 6)
#print("{} is {} and {} is {} and {}.".format(
#    philo.name, philo.age, mikey.name, mikey.age, philo.good))

#face recgnition text

#from resources.scripts.WebCam import *
#feed=get_feed(0)
#rval, frame=feed.read()


hostname="localhost"


# install flask

from flask import Flask

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
@app.route('/hello')
def hello():
    # Render the page
    return "Hello Python!"


app.run('localhost', 4449)



