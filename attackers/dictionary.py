import multiprocessing as mp
from itertools import product
LEET=str.maketrans({'a':'@','e':'3','i':'1','o':'0','s':'$','t':'7'})
def mutations(word):
 yield word
 yield word.capitalize()
 yield word.translate(LEET)
 for suffix in ('1','123','2024','2025','2026','!'):
  yield word+suffix;yield word.capitalize()+suffix
def _worker(args):
 kind,encoded,candidates=args
 from hashers.verify import verify
 for word in candidates:
  try:
   if verify(word,encoded,kind):return word
  except (ValueError,RuntimeError):raise
 return None
def attack(kind,encoded,words,workers=1):
 candidates=list(dict.fromkeys(c for w in words for c in mutations(w)))
 if workers<=1:return _worker((kind,encoded,candidates))
 chunks=[candidates[i::workers] for i in range(workers)]
 with mp.Pool(workers) as pool:
  for result in pool.imap_unordered(_worker,[(kind,encoded,c) for c in chunks]):
   if result:
    pool.terminate();return result
 return None
