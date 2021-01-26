import urllib.request
import json
from pprint import pprint

def make_http_post_request(url, values, headers):
    data = json.dumps(values).encode("utf-8")
    try:
        req = urllib.request.Request(url, data, headers)
        with urllib.request.urlopen(req) as f:
            res = f.read()
        task_id = res.decode()
        print(task_id)
        return task_id
    except Exception as e:
        pprint(e)


def post_scan_file_task() -> str:
    url = "http://localhost/v1.0/pc/files/scan"
    values = {
            "scan_path": ["C:\\Users\\Albert\\Desktop", r'D:\clouds\xa帝岚\4-信息共享\test-files'],
            "file_suffix": [".dwg", ".pdf"],
            "keywords_list": ["秘密", "机密"],
        }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    return make_http_post_request(url, values, headers)


def get_scan_status(task_id, page_size):
    url = "http://localhost/v1.0/pc/files/scan/status?task_id={}&page_size={}".format(task_id, page_size)
    contents = urllib.request.urlopen(url).read().decode()
    return contents


def test_get_scan_status():
    response = post_scan_file_task()
    json_res = json.loads(response)
    task_id = json_res.get('task_id')
    status = ''
    while status != 'finished':
        response = get_scan_status(task_id, 5)
        print(response)
        json_res = json.loads(response)
        if isinstance(json_res, dict):
            status = json_res.get('status')
            c = json_res.get('results')
            for i in c:
                print(i)
        else:
            print(json_res)
            break


if __name__ == '__main__':
    test_get_scan_status()
