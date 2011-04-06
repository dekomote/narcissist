import os
os.environ["NARCISSIST_SETTINGS"] = os.path.join(os.path.dirname( os.path.realpath( __file__ ) ), "settings.py")

from narcissist import app

if __name__=="__main__":
    app.run()
