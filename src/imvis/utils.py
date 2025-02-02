import os
import datetime

def newfolder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return 0
    else:
        return -1
    
def newfolder2(base, dirname):
    suffix=0
    fullpath = os.path.join(base, dirname)
    if not os.path.exists(fullpath):
        os.makedirs(fullpath)
        return fullpath
    while os.path.exists(fullpath+str(suffix)):
        suffix+=1
    os.makedirs(fullpath+str(suffix))
    return fullpath+"_"+str(suffix)

def newfilename(base, fname):
    if not os.path.exists(os.path.join(base, fname)):
        return os.path.join(base, fname)
    if '.' in fname:
        name, ext = fname.split('.')
        suffix = 0
        while os.path.exists(os.path.join(base, name+str(suffix)+'.'+ext)):
            suffix+=1
        return os.path.join(base, name+"_"+str(suffix)+'.'+ext)
    else:
        suffix = 0
        while os.path.exists(os.path.join(base, fname+str(suffix))):
            suffix+=1
        return os.path.join(base, fname+"_"+str(suffix))
    
def datetimestr_diff(datetimestr1, datetimestr2):
    """Calculate the time difference between two date time strings.
    Parameters
    ----------
    datetimestr1 : string
        Date time string 1.
    datetimestr2 : string
        Date time string 2.
    Returns
    -------
    diff : float
        Time difference in seconds.
    """
    # if decimal point is present, remove the decimal point and the following digits
    if '.' in datetimestr1:
        datetimestr1 = datetimestr1.split('.')[0]
    if '.' in datetimestr2:
        datetimestr2 = datetimestr2.split('.')[0]
    dt1 = datetime.datetime.strptime(datetimestr1, "%Y%m%d%H%M%S")
    dt2 = datetime.datetime.strptime(datetimestr2, "%Y%m%d%H%M%S")
    diff = (dt1 - dt2).total_seconds()
    return diff