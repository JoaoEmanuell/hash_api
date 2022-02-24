from hashlib import sha256

class Hash:
    
    def generate_hash(self, value : str) -> str:
        return sha256(value.encode('utf-8')).hexdigest()

    def compare_hash(self, value : str, hash : str) -> bool:
        if hash == self.generate_hash(value):
            return True
        return False