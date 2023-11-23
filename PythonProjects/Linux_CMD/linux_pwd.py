import os

### this code will work only when executed on Linux machine,
#if we are running on windows machine, it will open windows cmd prompt, and will look for cmd "pwd", and will through exception
#'pwd' is not recognized as an internal or external command,
#operable program or batch file.
stream = os.popen("pwd")
data = stream.read()
print(data)