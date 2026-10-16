import hashlib,unittest
from hashers.verify import verify
from strength.estimate import estimate
from attackers.dictionary import mutations
class AuditTests(unittest.TestCase):
 def test_sha256(self):self.assertTrue(verify('winter',hashlib.sha256(b'winter').hexdigest(),'sha256'))
 def test_mutations(self):self.assertIn('Winter123',list(mutations('winter')))
 def test_weak_flags(self):self.assertIn('common password',estimate('password')['patterns'])
if __name__=='__main__':unittest.main()
