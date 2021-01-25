import win32pipe, win32file


class NamedPipiClient:
    def __init__(self):
        self.server_address = r'\\.\pipe\audit_service'
        self._handle = None
        self._connect()

    def _connect(self):
        self._handle = win32file.CreateFile(
            self.server_address,
            win32file.GENERIC_READ | win32file.GENERIC_WRITE,
            0,
            None,
            win32file.OPEN_EXISTING,
            0,
            None
        )
        win32pipe.SetNamedPipeHandleState(self._handle, win32pipe.PIPE_READMODE_MESSAGE, None, None)

    def invoke_service_run(self, msg: str) -> bool:
        text = 'XADL_AUDIT' + msg
        sent = text.encode('utf-16-le')
        print(f'sent {len(sent)} bytes')
        win32file.WriteFile(self._handle, sent)
        _, resp = win32file.ReadFile(self._handle, 64 * 1024)
        print('recv', len(resp), resp)
        print(resp.decode('utf-16-le'))


if __name__ == '__main__':
    NamedPipiClient().invoke_service_run("uninstall client")
