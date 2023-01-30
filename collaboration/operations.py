class Basicoperations:
    def __init__(self) -> None:
        self.__a = a
        self.__b = b
    
    def sum(self):
        return self.__a + self.__b
    
    
    
    def division(self):
        if self.__b != 0:
            return self.__a / self.__b
        else:
            return "ZeroDivisionError"