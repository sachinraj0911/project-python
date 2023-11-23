import os


class OsError(Exception):
    pass


try:
    stream = os.popen("pwd")
    raise OsError
except OsError:
    print("CMD command is not applicable for windows OS")

