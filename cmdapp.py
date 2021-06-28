import flask
from flask import jsonify, render_template, request
import json
import subprocess 
import time     
from io import BufferedReader   
from flask_restful import Resource, Api


app = flask.Flask(__name__)
api = Api(app)

# global command   




class cmd_output(Resource):

    def get(self, command):
        respo = []
        proc = subprocess.Popen(
                command,            # CMD DOS COMMAND for IP CONFIGURATION 
                shell=True,
                stdout=subprocess.PIPE
            )
   
        for line in proc.stdout.readlines():
            respo.append(line.rstrip().decode("utf-8"))
            # yield line.rstrip().decode("utf-8")

        return {'respo': respo}

api.add_resource(cmd_output, '/cmd_output/<command>')


# Future UI

# @app.route("/", methods=['GET', 'POST'])
# def home():
#     global command
#     command = request.get_data().decode('utf-8')
#     return render_template("display.html")



if __name__ == '__main__':
    app.run(debug=True)