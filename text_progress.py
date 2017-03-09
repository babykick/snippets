"""
   Verious implements for text progress bar
   Refered from: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
"""
import time
import sys



def update_progress():
    for i in range(100):
        time.sleep(1)
        sys.stdout.write("\rcompleted %d%%" % i)
    sys.stdout.flush()


def update_progress2():
    import click

    with click.progressbar(range(1000000)) as bar:
        for i in bar:
            pass 

def update_progress3():
    from time import sleep  
    from random import random  
    from clint.textui import progress  
    
    for i in progress.bar(range(100)):
        sleep(random() * 0.2)

    for i in progress.dots(range(100)):
        sleep(random() * 0.2)


def update_progress4():
    import time
    from tqdm import tqdm
    for i in tqdm(range(100)):
        time.sleep(1)

print('Some lines already printed')
update_progress()