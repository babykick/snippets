"""
   Move all the files under root path recursively into root. 
"""
import os
import sys
import glob
import shutil

import fire

def flatten(path):
    for img in glob.glob(os.path.join(path, '**/*.*'), recursive=True):
        if os.path.isfile(img) and not img.endswith('.py') and \
        os.path.abspath(path) != os.path.dirname(os.path.abspath(img)):
            print(img)
            shutil.move(img, path)

def main():
    fire.Fire(flatten)

if __name__ == '__main__':
    main()