import hashlib
try:import bcrypt
except ImportError:bcrypt=None
SUPPORTED=('md5','sha1','sha256','ntlm','bcrypt')
def verify(candidate,encoded,kind):
 raw=candidate.encode('utf-8')
 if kind=='bcrypt':
  if bcrypt is None:raise RuntimeError('Install requirements.txt to verify bcrypt hashes')
  try:return bcrypt.checkpw(raw,encoded.encode())
  except ValueError:return False
 if kind=='ntlm':
  try:from Crypto.Hash import MD4
  except ImportError:raise RuntimeError('Install requirements.txt to verify NTLM hashes')
  h=MD4.new();h.update(candidate.encode('utf-16le'));actual=h.hexdigest()
 else:actual=hashlib.new(kind,raw).hexdigest()
 return actual.lower()==encoded.strip().lower()
