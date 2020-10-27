import os
import sys
import io
import argparse
import logging

# hack to make werkzeug work ... waiting for fix
# should be here before flask any imports
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask, Response, render_template
from flask_restplus import Resource, Api, reqparse, inputs
#from werkzeug.datastructures import FileStorage

# make it work with https
from werkzeug.middleware.proxy_fix import ProxyFix


# include ../../ directory to use modules in the root
sys.path.append(os.path.dirname(os.path.dirname((os.path.realpath(__file__)))))
# here you can import your own modules from root rootmodule.foo.bar


app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

app.wsgi_app = ProxyFix(app.wsgi_app)


# define web app pages here before api
@app.route("/")
def app_page():
    return render_template("index.html")

api = Api(
    app = app,
    version = "1.0",
    doc = "/api/",
    title = "API"
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--debug", help="Run in debug mode", action="store_true"
    )
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=args.debug, host="0.0.0.0", port=port)