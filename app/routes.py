from flask import Flask         # from the flask module import the Flask class

app = Flask(__name__)           # Create an instance of the Flask class. It is the OOP (Object oriented paradigm)

@app.get("/about")
@app.get("/")                   # Flask decorator that maps view functions to routes
def index():                    # view function
   me = {                       # python dictionary
      "first_name": "Thomas",
      "last_name": "Marcello",
      "hobbies": "Cooking",
      "is_online": True
   }
   return me                    # When you return a dict from a view function, it becomes JSON.
# @app.post()  
# @app.put()                 
# @app.patch()                 
# @app.delete()                 