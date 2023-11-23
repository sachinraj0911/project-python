from PythonProjects.MyRegularExp.to_get_valid_ip import to_get_valid_ipaddress

fp1 = open("RAJ.txt", 'r')
fp2 = open("file.txt", 'w+')
data = fp1.read()
print(data)
iplist = to_get_valid_ipaddress(data)
for ip in iplist:
    fp2.write(ip)
    fp2.write('\n')


fp1.close()
fp2.close()

