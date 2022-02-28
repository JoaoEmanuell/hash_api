# Global Imports

from hashlib import sha256

# Local Imports

from .validators.hash_validation import HashValidation

class Hash:
    
    def generate_hash(self, value : str) -> str:
        try : 
            value_validate = HashValidation(value)._validate()
            self.__value = sha256(value_validate).hexdigest()
        except (ValueError, TypeError) as e:
            return f'Error {e}'
        else :
            return self.__value

    def compare_hash(self, value : str, hash : str) -> bool:
        hash = HashValidation(hash)._validate()
        if hash == self.generate_hash(value):
            return True
        return False