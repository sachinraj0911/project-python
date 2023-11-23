import os
import pexpect

ip = "1.1.1.1"

console = "str("telnet") + str(ip)"

con = pexpect.expect(console)
a = con.expect("~]$", timout = 10)
a.sendline("\r")
output = a.sendline("pwd")


