#!/usr/bin/env/ python
import os
import subprocess
from multiprocessing import Pool

def files(archivos):
   #OS WALK MODULE RETURN A TUPLE WITH DIRECTORIES, AND FILES, UNPACKED THEM JUST TO GET THE DIRETORY NAME
    directory, files, files_2 = archivos
    return driectory

def backup(file):
    source = file
    destiny = #PUT YOUR BACKUP PATH HERE#
    subprocess.call(['rsync','=arq', source, destiny])
 

if __name__ == '__main__':
    lista = list(os.walk(os.getcwd()))
    with ProcessPoolExecutor(max_workers = 4) as executor:
      process_1 = list(executor.map(files, lista))
      process_2 = executor.map(backup, process_1)
