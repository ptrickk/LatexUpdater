import os
import time

print(os.system('dir'))

def main(file):
    while True:
        print('Compile ' + file)
        os.system('pdflatex ' + file)
        time.sleep(2.0)

if __name__ == "__main__":
    file = input("Type in filename (.tex): ")
    main(file)
