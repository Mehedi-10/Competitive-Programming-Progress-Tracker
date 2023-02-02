from .toph import TOPH as tp
from .codechef import CODECHEF as cc
from .codeforces import CODEFORCES as cf
from .lightoj import LIGHTOJ as loj
from .atcoder import ATCODER as ac

def get_info(cf_h:str,toph_h:str,ac_h:str,loj_h:str,cc_h:str):
    otp=tp(toph_h)
    ocf=cf(cf_h)
    # oac=ac(ac_h)
    # oloj=loj(loj_h)
    # occ=cc(cc_h)
    return {'rank':[ocf.rating,otp.rating]}

    # return {'rank':[ocf.rating,otp.rating,oac.rating,oloj.rating,occ.rating]}



# rating
# highest_rating
# rank loj

