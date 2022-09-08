class Designacion:
    __añoDesignacion: str
    __justicia: str
    __cargoTipo: str
    __instanciaTipo: str
    __materia: str
    __cantidadVarones: int
    __cantidadMujeres: int

    def __init__(self, añoDesignacion, justicia, cargoTipo, instanciaTipo, materia, cantidadVarones, cantidadMujeres) -> None:
        self.__añoDesignacion = añoDesignacion
        self.__justicia = justicia
        self.__cargoTipo = cargoTipo
        self.__instanciaTipo = instanciaTipo
        self.__materia = materia
        self.__cantidadVarones = cantidadVarones
        self.__cantidadMujeres = cantidadMujeres
    

    def getAñoDesignacion(self) -> str:
        return self.__añoDesignacion
    
    def getJusticia(self) -> str:
        return self.__justicia
    
    def getCargoTipo(self) -> str:
        return self.__cargoTipo
    
    def getInstanciaTipo(self) -> str:
        return self.__instanciaTipo

    def getMateria(self) -> str:
        return self.__materia
    
    def getCantidadVarones(self) -> int:
        return self.__cantidadVarones
    
    def getCantidadMujeres(self) -> int:
        return self.__cantidadMujeres
    
    