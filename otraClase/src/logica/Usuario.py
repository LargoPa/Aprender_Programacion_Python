
class Usuario:
    def __init__(self, id, nombre, email):
        self.__id = id
        self.__nombre = nombre
        self.__email = email

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, nuevo_email):
        self.__email = nuevo_email



