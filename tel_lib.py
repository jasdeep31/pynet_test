import telnetlib
import time

TELNET_PORT = 136
TELNET_TIMEOUT = 6

def main():
    ip_addr = "171.79.57.236"
    username = "jsingh8"
    password = "Whirlp@5L"

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()    
    print output
    
    remote_conn.write("terminal length 0" + '\n')
    time.sleep(1)
    
    remote_conn.write("show version" + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output
    
    remote_conn.close()

if __name__ == "__main__":
    main()
