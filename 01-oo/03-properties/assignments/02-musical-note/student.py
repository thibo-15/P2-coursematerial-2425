class MusicalNote:
    def __init__ (self, name, pitch):
        self.__name = name
        self.__pitch = pitch

    @property
    def name(self):
        return self.__name
    
    @property
    def pitch(self):
        return self.__pitch
    

# een readonly property is een property die je enkel kan lezen 
# en niet kan schrijven maw een private property
        
    