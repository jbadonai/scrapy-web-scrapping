import subprocess


class Available():

    def available():
        result = subprocess.getoutput('ping www.google.com -n 1')
        if str(result).lower().__contains__('ttl='):
            return True
        else:
            return False