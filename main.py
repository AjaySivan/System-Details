import subprocess
import speedtest
import pyautogui
import os
import platform
import cpuinfo
import multiprocessing
import psutil
from win32api import GetSystemMetrics
from getmac import get_mac_address as gma
import public_ip as ip


def soft_list():
    Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
    a = str(Data)
    try:
        for i in range(len(a)):
            print(a.split("\\r\\r\\n")[6:][i])
    except IndexError as e:
        print("All Done")


def speed_test():
    s = speedtest.Speedtest()
    download_speed = s.download() / 1_000_000
    upload_speed = s.upload() / 1_000_000
    print("Download speed:", round(download_speed, 2), "Mbps")
    print("Upload speed:", round(upload_speed, 2), "Mbps")


def win_size():
    screensize = pyautogui.size()
    print("Screen size : ", screensize)


def cpu():
    cpu_info = {}
    cpu_info['brand_raw'] = cpuinfo.get_cpu_info()['brand_raw']
    cpu_info['brand'] = cpuinfo.get_cpu_info()['brand']
    cpu_info['cores'] = cpuinfo.get_cpu_info()['cores']
    cpu_info['threads'] = cpuinfo.get_cpu_info()['threads']
    print(f'brand_raw: {cpu_info["brand_raw"]}')
    print(f'brand: {cpu_info["brand"]}')
    print(f'CPU cores: {cpu_info["cores"]}')
    print(f'CPU threads: {cpu_info["threads"]}')


def get_gpu_model():
    result = subprocess.check_output(['wmic', 'path', 'win32_videocontroller', 'get', 'caption'], text=True)
    gpu_model = result.strip().split('\n')[1].strip()
    if gpu_model:
        print("GPU Model:", gpu_model)
    else:
        print("GPU information not available.")


def ram():
    total_ram = psutil.virtual_memory().total
    total_ram_gb = total_ram / 1024 / 1024 / 1024
    print("Total RAM:", round(total_ram_gb, 2), "GB")


def window_size():
    print("System Metrics : ")
    print("Width =", GetSystemMetrics(0))
    print("Height =", GetSystemMetrics(1))


def mac_address():
    print("Mac Address : ", gma())


def public_ip():
    value = ip.get()
    print("Public IP :", value)


def windows():
    print(platform.system() + " " + platform.release())


if __name__ == "__main__":
    print("Welcome to the Total System Description Solution")
    print("""Choose your option:
             \n1: Software List
             \n2: Speed Test
             \n3: Screen Resolution
             \n4: CPU 
             \n5: GPU
             \n6: RAM
             \n7: Screen Size
             \n8: MAC Address
             \n9: Public IP
             \n10:Windows Version
             \n11: Exit""")

    switch_dict = {
        1: soft_list,
        2: speed_test,
        3: win_size,
        4: cpu,
        5: get_gpu_model,
        6: ram,
        7: window_size,
        8: mac_address,
        9: public_ip,
        10: windows,
        11: exit
    }
while True:
    try:
        case_number = int(input("Enter the case number (1-11): "))
        selected_case = switch_dict.get(case_number, lambda: print("Invalid case number"))
        selected_case()
    except ValueError:
        print("Please enter a valid number.")
