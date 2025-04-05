import time
import random
import sys
from datetime import datetime
from colorama import init, Fore
import itertools

init(autoreset=True)

COLORS = [Fore.RED]
color_cycle = itertools.cycle(COLORS)

def generate_fake_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_log(packet_num, response_time):
    ip = generate_fake_ip()
    packets = Fore.GREEN + str(packet_num) + Fore.RESET
    response = Fore.GREEN + f"{response_time:.3f}s" + Fore.RESET
    timestamp = next(color_cycle) + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Fore.RESET
    return f"[{timestamp}] Attack from {ip} - Packet {packets} - Response Time: {response}"

def simulate_ddos(max_packets):
    print(Fore.RED + "\nStarting DDoS simulation... Press CTRL+C to stop.\n")
    try:
        packet_num = 1
        response_time = random.uniform(0.1, 0.5)
        last_increase = time.time()

        while packet_num <= max_packets:
            log = generate_log(packet_num, response_time)
            print(log)
            time.sleep(0.06)

            # 37% chance to keep stable, 63% chance to increase
            if time.time() - last_increase >= 2:
                if random.random() > 0.37:
                    response_time *= 1.07  # Increase by 7%
                last_increase = time.time()

            packet_num += 1
    except KeyboardInterrupt:
        print(Fore.WHITE + "\nDDoS simulation stopped.")
        sys.exit(0)

if __name__ == "__main__":
    try:
        max_packets = int(input("Enter the number of packets to send (max 5,000,000): "))
        if max_packets > 5000000:
            print(Fore.RED + "Max limit is 5,000,000. Setting to 5,000,000.")
            max_packets = 5000000
        simulate_ddos(max_packets)
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number.")