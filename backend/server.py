from flask import Flask
import json
from flask import request

from backend.event_center import GlobalStatus
from backend.v1_0.pc import get_host_information
from backend.v1_0.pc import get_network_information


app = Flask(__name__)


@app.route('/v1.0/pc/information')
def host_info():
   s = get_host_information()
   return json.dumps(s)


@app.route('/v1.0/pc/network')
def network_info():
   s = get_network_information()
   return json.dumps(s)

# https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
@app.route('/v1.0/pc/files/scan', methods=['POST'])
def scan_file():
   data = request.get_json()
   print(data)
   scan_path = data.get('scan_path')
   file_suffix = data.get('file_suffix')
   keywords_list = data.get('keywords_list')
   response = {
        "status": "success",
        "task_id": 21,
    }
   return json.dumps(response)


@app.route('/v1.0/pc/files/scan/status')
def get_scan_status():
   task_id = request.args.get("task_id")
   if task_id is None:
      return "task_id should not be none"
   else:
      print('task_id is', task_id)
   r = GlobalStatus.get_scan_status(task_id)
   return json.dumps(r)


if __name__ == '__main__':
   host = '0.0.0.0'
   port = '80'
   app.run(host, port)