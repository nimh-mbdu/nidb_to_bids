############## Codes ###################
## change the ‘basedir’ to your python script

import os
basedir = '/EDB/MBDU/dipta_working'

## Changing all the files name(start with S) to “sub-***” and “ses-***”

for path, dirs, files in os.walk(basedir):
    #print(path)
    for f in files:
        if f.startswith("S"):
            #print(path)
            fnparts = f.split('_')
            subn = fnparts[0]
            sesn = int(fnparts[1])
            rest_of_fn = '_'.join(fnparts[2:])
            rnmf=f'sub-{subn}_ses-{sesn:02d}_{rest_of_fn}'
            print(rnmf)
            os.rename(os.path.join(path, f), os.path.join(path, rnmf))



## Changing all the dir name(start with S)to “sub-***”

for path, dirs, files in os.walk(basedir):
    #print(path)
    for d in dirs:
        if d.startswith("S"):
            #print(path)
            rnmd='sub-'+d
            #print(rnmd)
            os.rename(os.path.join(path, d), os.path.join(path, rnmd))



## Changing all the dir name(start with Integer)to “ses-***”

for d in os.listdir(basedir):
    if d.startswith("sub"):
        print(d)
        path=os.path.join(basedir,d)
        print(path)
        for dr in os.listdir(path):
            print(dr)
            sesn = int(dr)
            rnmd=f'ses-{sesn:02d}'
            print(rnmd)
            os.rename(os.path.join(path, dr), os.path.join(path, rnmd))