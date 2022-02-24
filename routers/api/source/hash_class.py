# Global Imports

from hashlib import sha256

# Local Imports

from .validators.hash_validation import HashValidation

class Hash:
    
    def generate_hash(self, value : str) -> str:
        try : 
            self.__value = sha256(value.encode('utf-8')).hexdigest()
        except ValueError :
            return 'Error'
        else :
            return self.__value

    def compare_hash(self, value : str, hash : str) -> bool:
        if hash == self.generate_hash(value):
            return True
        return False