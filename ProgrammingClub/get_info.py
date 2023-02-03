import time

from .toph import TOPH as tp
from .codechef import CODECHEF as cc
from .codeforces import CODEFORCES as cf
from .lightoj import LIGHTOJ as loj
from .atcoder import ATCODER as ac

def get_info(cf_h:str,toph_h:str,ac_h:str,loj_h:str,cc_h:str):
    ojdata={}

    otp=tp(toph_h)
    if not otp.status:
        time.sleep(10)
    else:
        ojdata.setdefault('toph')
        ojdata['toph']=otp
    time.sleep(10)

    ocf=cf(cf_h)
    if not ocf.status:
        time.sleep(10)
    else:
        ojdata.setdefault('cf')
        ojdata['cf']=ocf
    time.sleep(10)

    oac=ac(ac_h)
    if not oac.status:
        time.sleep(10)
    else:
        ojdata.setdefault('atcoder')
        ojdata['atcoder']=oac
    time.sleep(10)

    oloj=loj(loj_h)
    if not oloj.status:
        time.sleep(10)
    else:
        ojdata.setdefault('lightoj')
        ojdata['lightoj']=oloj
    time.sleep(10)

    occ=cc(cc_h)
    if not occ.status:
        time.sleep(10)
    else:
        ojdata.setdefault('codechef')
        ojdata['codechef']=occ
    print(ojdata)
    return ojdata


# rating
# highest_rating
# rank loj

