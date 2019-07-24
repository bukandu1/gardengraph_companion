from flask import (Flask, session, redirect, render_template, flash, 
                    request, url_for, jsonify)
import mongoengine
from plants import Plants

app = Flask(__name__)

#Set key to use sessions and debug toolbar
app.secret_key = os.environ['FLASK_SESSION_KEY']
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

@app.route('/', methods=["GET"])
def display_login():
    """Home page for Garden Graph app"""
    return render_template("homepage.html")


def main():
    mongo_setup.global_init()

    print_header()

    try:
        while True:
            if find_user_intent() == 'book':
                program_guests.run()
            else:
                program_hosts.run()
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    main()