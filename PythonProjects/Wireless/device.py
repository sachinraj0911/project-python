
import pexpect
import time

def hostname_lookup(console, port):
    connection = "telnet " +console +" " +str(port)
    c = pexpect.spawn(connection)
    #login happening here
    c.sendline('\r')
    c.expect(['>', '#'])
    c.sendline('\n')
    c.expect(['>', '#'])
    h = c.before
    hostname = (h.lstrip()).decode('utf-8')
    return hostname

def iol_up(console, port):
    connection = "telnet " +console +" " +str(port)
    c = pexpect.spawn(connection) #login happening here
    time.sleep(28)
    c.sendline('\r')
    #c.expect('Would you like to enter the initial configuration dialog? [yes/no]:')
    c.sendline('no\r')
    c.sendline('\n')
    c.sendline('\n')
    c.sendline('\n')
    c.sendline('\n')
    c.sendline('\n')
    c.sendline('\n')
    c.sendline('\n')
    time.sleep(15)
    c.sendline('\n')
    c.sendline('\n')
    c.sendline('\n')
    time.sleep(5)
    c.close
