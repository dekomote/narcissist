import os, sys
os.environ["NARCISSIST_SETTINGS"] = os.path.join(os.path.dirname( os.path.realpath( __file__ ) ), "settings.py")
sys.path.append(os.path.dirname( os.path.realpath( __file__ ) ))

from narcissist import app as application

if __name__=="__main__":
    application.run()
