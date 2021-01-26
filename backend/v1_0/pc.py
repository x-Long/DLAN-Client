def get_host_information() -> dict:
    pc_info = {
    "pc_type": "VivoBook",
    "pc_name": "Albert's Laptop",
    "mother_board_model": "ASUST eK COMPUTERINC.",
    "cd_drive": [],
    "ram_size": "16GB",
    "processor_info": "Inter(R) Core(TM) i7-8570U CPU 1.8GHz",
    }
    return pc_info


def get_network_information() -> list:
    network_info = [
        {
            "mac": "00:50:56:C0:00:08",
            "ip": "192.168.114.1",
            "desc": "有线网卡",
        },
        {
            "mac": "74:E5:F9:90:40:B6",
            "ip": "192.168.4.101",
            "desc": "无线网卡",
        }
    ]
    return network_info
