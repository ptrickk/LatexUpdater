import os
import sys
import time
from datetime import datetime

def main(remote):
    print('SELECTED REMOTE REPOSITORY: ' + remote)
    while True:    
        timestamp = datetime.fromtimestamp( time.time()).strftime('%d-%m-%Y %H:%M:%S')
        os.system('git add .')
        os.system('git commit -m \"auto commit at: ' + timestamp + '\n')
        os.system('git push ' + remote)
        time.sleep(30)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        main('origin')
    else:
        main(sys.argv[1])
