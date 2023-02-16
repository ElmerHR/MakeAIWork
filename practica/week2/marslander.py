from dataclasses import dataclasses

@dataclasses
class Marslander:
    length: int
    width: float
    weight: int
    deckHeight: tuple
    robotArmLength: float
    numberOfSolarPanels: int
    scienceInstruments: tuple
    image: str
    
    