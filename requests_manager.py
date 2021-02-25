import json
import urllib.request
from utlis import singleton
from log_utils import logger

@singleton
class RequestManager:
    def __init__(self):
        self.host = 'localhost'
        self.port = None
        self.base_url = None

    def get_base_url(self):
        return self.base_url

    def on_port_ready(self, port: int):
        self.port = port
        self.base_url = f'http://{self.host}:{self.port}'

    def is_server_ready(self):
        return self.base_url != None

    def make_get_request(self, router_name:str):
        url = f'{self.base_url}{router_name}'
        try:
            logger.info(f'request {url}')
            output = urllib.request.urlopen(url).read().decode()
            logger.debug(f'output: {output}')
            objs = json.loads(output)
            return objs
        except Exception as ex:
            logger.exception(f'error on {url}', exc_info=ex)

    def make_post_request(self, router_name:str, values):
        url = f'{self.base_url}{router_name}'
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        data = json.dumps(values).encode("utf-8")
        try:
            req = urllib.request.Request(url, data, headers)
            with urllib.request.urlopen(req) as f:
                output = f.read()
            logger.debug(f'output: {output}')
            return json.loads(output.decode())
        except Exception as ex:
            logger.exception(f'error on {url}', exc_info=ex)


if __name__ == '__main__':
    RequestManager.on_port_ready(8081)
    aaa = RequestManager.make_get_request('/v1.0/app/footer/info')
