import random

class _secrets:
    _sysrand = random.SystemRandom()
    
    def randbits(self, k):
        return self._sysrand.getrandbits(k)
        
    def choice(self, sequence):
        return self._sysrand.choice(sequence)
    
    def randbelow(self, n):
        return self._sysrand.randrange(n)
    
    def token_bytes(self, nbytes=None):
        if nbytes is None:
            nbytes = 32
        return self._sysrand.getrandbits(nbytes * 8).to_bytes(nbytes, 'little')
    
    def token_hex(self, nbytes=None):
        return self.token_bytes(nbytes).hex()
    
    def compare_digest(self, a, b):
        if isinstance(a, str):
            a = a.encode('utf-8')
        if isinstance(b, str):
            b = b.encode('utf-8')
            
        if len(a) != len(b):
            return False
        result = 0
        for x, y in zip(a, b):
            result |= x ^ y
        return result == 0

import sys
sys.modules['secrets'] = _secrets()
