import math,re
COMMON={'password','password1','123456','qwerty','letmein','admin','welcome'}
WALKS=('qwerty','asdf','zxcv','12345','qazwsx')
def estimate(password):
 classes=sum(bool(re.search(p,password)) for p in (r'[a-z]',r'[A-Z]',r'\d',r'[^A-Za-z0-9]'))
 pool=sum((26 if re.search(p,password) else 0) for p in (r'[a-z]',r'[A-Z]'))+10*bool(re.search(r'\d',password))+32*bool(re.search(r'[^A-Za-z0-9]',password))
 entropy=round(len(password)*math.log2(max(pool,1)),1)
 lower=password.lower();flags=[]
 if lower in COMMON:flags.append('common password')
 if any(w in lower for w in WALKS):flags.append('keyboard walk')
 if re.search(r'(.)\1{2,}',password):flags.append('repeated characters')
 if len(password)<12:flags.append('short length')
 score=min(4,max(0,(len(password)>=12)+(len(password)>=16)+(classes>=3)+(entropy>=60))-(lower in COMMON))
 return {'length':len(password),'estimated_entropy_bits':entropy,'score_0_to_4':int(score),'patterns':flags}
