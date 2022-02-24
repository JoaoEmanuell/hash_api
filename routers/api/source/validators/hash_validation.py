class HashValidation:
    def __init__(self, value : str) -> None:
        self.__value = value

    def _validate(self) -> str :
        self.__value = self.__value.strip()
        self.__len_verification()
        return self.__value
    
    def __len_verification(self):
        if len(self.__value) == 0 :
            raise ValueError('Value cannot be empty')