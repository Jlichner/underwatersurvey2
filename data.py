from dataclasses import dataclass
from enum import Enum

class Landmark(Enum):
    MOORING_BLOCK = 0
    SKELETON = 1
    CAR = 2
    UMBRELLA = 3
    ANCHOR = 4
    CONROY = 5
    ISLANDER_T = 6
    ROCK_ISLAND_T = 7
    WAGON_WHEELS = 8
    LISAS_GIFT = 9
    KIBBETTS = 10
    ROWBOAT = 11
    OXYGEN_TANKS = 12


@dataclass(frozen=True)
class AbstractLine:
    color: str
    linestyle: str
    length: int = 0
    angle: int = 0.0
    flip_text_side: bool = False
    alt_text: str = None

@dataclass(frozen=True)
class SurveyedLine(AbstractLine):
    color: str = 'black' 
    linestyle: str = 'solid'

@dataclass(frozen=True)
class UnsurveyedLine(AbstractLine):
    color: str = 'black'
    linestyle: str = 'dotted'

@dataclass(frozen=True)
class RemovedLine(AbstractLine):
    color: str = 'lightgrey'
    linestyle: str = 'solid'

@dataclass(frozen=True)
class Jump:
    length: int = 0
    angle: int = 0.0

@dataclass(frozen=True)
class SaveLandmark:
    landmark: Landmark = None
    path: str = None

@dataclass(frozen=True)
class Stake:
    color: str = 'brown' 
    marker: str = 's'
    zorder: int = 3

@dataclass(frozen=True)
class RemovedStake:
    color: str = 'lightgrey' 
    marker: str = 's'

@dataclass(frozen=True)
class TieOff:
    color: str = 'blue' 
    marker: str = 'h'
    zorder: int = 3

@dataclass(frozen=True)
class HomeArrow:
    distance: int = 9
    angle: int = 0.0

PokerRun = (
    UnsurveyedLine(length=25, angle=0, alt_text='To shore', flip_text_side=True),
    HomeArrow(angle=180),
    Stake(),
    SurveyedLine(length=50, angle=300),
    SaveLandmark(Landmark.SKELETON, path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-500-skull@3x.png'),
    SurveyedLine(length=87, angle=60),
    Stake(),
    SurveyedLine(length=72, angle=50),
    TieOff(),
    SurveyedLine(length=35, angle=60, color='red'),
    TieOff(),
    SurveyedLine(length=15, angle=60),
    SaveLandmark(landmark=Landmark.CAR, path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-6-car@3x.png'),
    HomeArrow(angle=240),
    Jump(length=0, angle=0),
    SurveyedLine(length=95, angle=300),
    SaveLandmark(landmark=Landmark.UMBRELLA, path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-14-beach-umbrella@3x.png'),
    Jump(length=0, angle=0),
    SurveyedLine(length=150, angle=240),
    SaveLandmark(landmark=Landmark.ANCHOR, path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-258-anchor@3x.png'),
    Jump(length=0, angle=0),
    HomeArrow(angle=175),
    SurveyedLine(length=63, angle=175),
    Jump(length=0, angle=0), # Lower platform
    SurveyedLine(length=66, angle=290),
    Stake(),
    SurveyedLine(length=15, angle=240),
    SaveLandmark(landmark=Landmark.CONROY),
    HomeArrow(angle=150),
    Jump(length=0, angle=0),
    SurveyedLine(length=49, angle=150),
    Stake(),
    UnsurveyedLine(length=50, angle=210, alt_text='To Islander'),
    Jump(length=50, angle=30),
    HomeArrow(angle=90),
    SurveyedLine(length=85, angle=90),
)

CarToKibbetts = (
    UnsurveyedLine(length=270, angle=50),
    Stake(),
    SurveyedLine(length=17, angle=340),
    SaveLandmark(landmark=Landmark.WAGON_WHEELS, path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-677-car-wheel@3x.png'),
    Jump(length=17, angle=160),
    UnsurveyedLine(length=396, angle=50),
    SaveLandmark(landmark=Landmark.LISAS_GIFT, path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-70-gift@3x.png'),
    UnsurveyedLine(length=50, angle=320, alt_text=''),
    Jump(length=50, angle=140),
    UnsurveyedLine(length=268, angle=70),
    SaveLandmark(landmark=Landmark.KIBBETTS),
)

UmbrellaToRockIsland = (
    SurveyedLine(length=18, angle=20),
    Stake(),
    SurveyedLine(length=21, angle=10),
    Stake(),
    SurveyedLine(length=52, angle=20),
    Stake(),
    SurveyedLine(length=25, angle=20),
    Stake(),
    SurveyedLine(length=87, angle=20),
    Stake(),
    SurveyedLine(length=29, angle=10),
    Stake(),
    SurveyedLine(length=27, angle=20),
    Stake(),
    SurveyedLine(length=38, angle=5),
    Stake(),
    SurveyedLine(length=68, angle=10),
    Stake(),
    SurveyedLine(length=27, angle=0),
    TieOff(), # ROCK
    SurveyedLine(length=18, angle=40),
    Stake(),
    SurveyedLine(length=39, angle=0),
    Stake(),
    SurveyedLine(length=35, angle=355),
    Stake(),
    SurveyedLine(length=17, angle=10),
    Stake(),
    SurveyedLine(length=17, angle=0),
    Stake(),
    SurveyedLine(length=23, angle=0),
    Stake(),
    SurveyedLine(length=25, angle=0),
    Stake(),
    SurveyedLine(length=20, angle=10),
    Stake(),
    SurveyedLine(length=20, angle=0),
    Stake(),
    SurveyedLine(length=17, angle=0),
    Stake(),
    SurveyedLine(length=13, angle=0),
    Stake(),
    SurveyedLine(length=23, angle=0),
    Stake(),
    SurveyedLine(length=27, angle=0),
    Stake(),
    SurveyedLine(length=33.5, angle=348),
    Stake(),
    SurveyedLine(length=23, angle=350),
    Stake(),
    SurveyedLine(length=27, angle=345),
    Stake(),
    SurveyedLine(length=22, angle=310, flip_text_side=True),
    SurveyedLine(length=15, angle=40),
    SaveLandmark(Landmark.ROWBOAT, path='icons/rowboat.png'),
    Jump(length=15, angle=220),
    SurveyedLine(length=15, angle=315, flip_text_side=True),
    Stake(),
    SurveyedLine(length=16, angle=320),
    Stake(),
    SurveyedLine(length=24, angle=330),
    Stake(),
    SurveyedLine(length=22, angle=310),
    Stake(),
    SurveyedLine(length=24, angle=325),
    Stake(),
    SurveyedLine(length=15, angle=325),
    Stake(),
    SurveyedLine(length=15, angle=325),
    Stake(),
    SaveLandmark(Landmark.ROCK_ISLAND_T)
    )

UmbrellaToOxygenTanks = (
    SurveyedLine(length=3, angle=340, alt_text=''),
    Stake(zorder=2),
    SurveyedLine(length=49, angle=340),
    Stake(),
    SurveyedLine(length=49, angle=335),
    Stake(),
    SurveyedLine(length=49, angle=320),
    Stake(),
    SurveyedLine(length=13, angle=340),
    TieOff(), # BARREL
    SurveyedLine(length=28, angle=300),
    Stake(),
    SurveyedLine(length=40, angle=280),
    TieOff(), # ROCK1
    SurveyedLine(length=34, angle=215),
    TieOff(), # ROCK2
    SurveyedLine(length=32, angle=220),
    TieOff(), # ROCK3
    SurveyedLine(length=46, angle=280),
    Stake(),
    SurveyedLine(length=35, angle=280),
    Stake(),
    SurveyedLine(length=48, angle=235),
    Stake(),
    SurveyedLine(length=48, angle=240),
    Stake(),
    SurveyedLine(length=24, angle=280),
    SaveLandmark(Landmark.OXYGEN_TANKS, path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-256-oxygen-bottles@3x.png'),
)

RockIslandTNorthwest = (
    SurveyedLine(length=35, angle=225),
    Stake(),
    SurveyedLine(length=54, angle=235),
    Stake(),
    SurveyedLine(length=50, angle=240),
    Stake(),
    SurveyedLine(length=51, angle=240),
    Stake(),
    SurveyedLine(length=53, angle=240),
    Stake(),
    SurveyedLine(length=53, angle=220),
    Stake(),
    SurveyedLine(length=52, angle=220),
    Stake(),
    SurveyedLine(length=52, angle=235),
    Stake(),
    SurveyedLine(length=48, angle=220),
    Stake(),
    SurveyedLine(length=48, angle=250),
    UnsurveyedLine(length=50, angle=135, alt_text='Broken'),
    Jump(length=50, angle=315),
    TieOff(),
    SurveyedLine(length=72, angle=220),
    TieOff(),
    UnsurveyedLine(length=25, angle=240, alt_text=''),
    )

RockIslandTSoutheast = (
    UnsurveyedLine(length=50, angle=45, alt_text=''),
    )
