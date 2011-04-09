import os
#setting the settings.py path to NARCISSIST_SETTINGS env var. Important for
#the WSGI app
os.environ["NARCISSIST_SETTINGS"] = os.path.join(os.path.dirname( os.path.realpath( __file__ ) ), "settings.py")

from narcissist import app

if __name__=="__main__":
    #If you want debug mode, call this function with debug=True or add
    #DEBUG = True to settings.py
    app.run()
