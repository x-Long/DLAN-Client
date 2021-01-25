import urllib.request
import json
from pprint import pprint

def make_http_post_request(url, values, headers):
    data = json.dumps(values).encode("utf-8")
    try:
        req = urllib.request.Request(url, data, headers)
        with urllib.request.urlopen(req) as f:
            res = f.read()
        pprint(res.decode())
    except Exception as e:
        pprint(e)


def test_files_scan():
    url = "http://localhost/v1.0/pc/files/scan"
    values = {
            "scan_path": ["C:\\Users\\Albert", "D:\\", "E:\\"],
            "file_suffix": [".pdf", ".docx", ".xlsx"],
            "keywords_list": ["秘密", "机密"],
        }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    make_http_post_request(url, values, headers)


if __name__ == '__main__':
    test_files_scan()