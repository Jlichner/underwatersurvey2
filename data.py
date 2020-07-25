from dataclasses import dataclass
from enum import Enum

#####
#
# Surveyers:
#   Christian Lundkvist
#   Stephanie Yang
#   Lisa Goodlin
#   Doug Dwyer
#   Ben Rother
#   JP Vanier
#   Scott Fuller
#   Mike ???
#
#####

class Landmark(Enum):
    DISTANCE_MEASURE = 0
    CAR = 1
    CONROY = 2
    FOUR_WAY = 3
    ISLANDER_T = 4
    KIBBETTS = 5
    LISAS_GIFT = 6
    MOORING_BLOCK = 7
    MY_BOAT = 8 # For the README
    OXYGEN_TANKS = 9
    PLATFORM_SW = 10
    ROCK_ISLAND_T = 11
    ROWBOAT = 12
    SKELETON = 13
    UMBRELLA = 14
    WAGON_WHEELS = 15
    NATES_TIEOFF = 16
    BYPASS_END_SIXTY_FOOT = 17
    BYPASS_END_JJJ = 18
    ROCK_ISLAND_BOTTLE = 19
    BOBS_ARROW = 20
    EMMA_MUNSEN = 21
    ANCHOR = 22

@dataclass(frozen=True)
class AbstractLine:
    color: str
    linestyle: str
    length_ft: int = 0
    length_in: int = 0
    angle: int = 0.0
    flip_text_side: bool = False
    alt_text: str = None
    text_rotation: int = None
    include_in_total_surveyed: bool = True

@dataclass(frozen=True)
class SurveyedLine(AbstractLine):
    color: str = 'black' 
    linestyle: str = 'solid'

@dataclass(frozen=True)
class UnsurveyedLine(AbstractLine):
    color: str = 'black'
    linestyle: str = 'dotted'
    include_in_total_surveyed = False

@dataclass(frozen=True)
class RemovedLine(AbstractLine):
    color: str = 'lightgrey'
    linestyle: str = 'solid'

@dataclass(frozen=True)
class Jump:
    length_ft: int = 0
    length_in: int = 0
    angle: int = 0.0

@dataclass(frozen=True)
class SaveLandmark:
    landmark: Landmark = None
    icon_path: str = None
    zoom: int = 52

@dataclass(frozen=True)
class Stake:
    color: str = 'brown' 
    marker: str = 's'
    markersize: int = 5
    zorder: int = 3
    text: str = None
    text_rotation: int = 0

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
class Arrow:
    distance: int = 10 # default for home arrows
    angle: int = 0.0
    color: str = 'white'

PokerRun = (
    UnsurveyedLine(length_ft=25, angle=0, alt_text='To shore', text_rotation=270),
    Arrow(angle=180),
    Arrow(distance=18, angle=180),
    Stake(),
    SurveyedLine(length_ft=50, angle=300),
    SaveLandmark(Landmark.SKELETON, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-500-skull@3x.png'),
    SurveyedLine(length_ft=87, angle=60),
    Stake(),
    SurveyedLine(length_ft=72, angle=50),
    TieOff(),
    SurveyedLine(length_ft=35, angle=60, color='red'),
    TieOff(),
    SurveyedLine(length_ft=15, angle=60),
    SaveLandmark(landmark=Landmark.CAR, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-6-car@3x.png'),
    Arrow(angle=240),
    Jump(length_ft=0, angle=0),
    SurveyedLine(length_ft=95, angle=300),
    SaveLandmark(landmark=Landmark.UMBRELLA, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-14-beach-umbrella@3x.png'),
    Jump(length_ft=0, angle=0),
    SurveyedLine(length_ft=150, angle=240),
    SaveLandmark(landmark=Landmark.ANCHOR, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-258-anchor@3x.png'),
    Jump(length_ft=0, angle=0),
    Arrow(angle=175),
    SurveyedLine(length_ft=63, angle=175),
    Jump(length_ft=0, angle=0), # Lower platform
    SurveyedLine(length_ft=66, angle=290),
    TieOff(),
    SurveyedLine(length_ft=15, angle=240, alt_text=''),
    SaveLandmark(landmark=Landmark.CONROY, icon_path='icons/conroy.png', zoom=12),
    Arrow(angle=150),
    Jump(length_ft=0, angle=0),
    SurveyedLine(length_ft=49, angle=160),
    TieOff(),
    SaveLandmark(landmark=Landmark.PLATFORM_SW),
    Arrow(angle=90),
    SurveyedLine(length_ft=84, angle=85),
)

CarToKibbetts = (
    UnsurveyedLine(length_ft=270, angle=50, include_in_total_surveyed=True),
    Stake(),
    SurveyedLine(length_ft=17, angle=340),
    SaveLandmark(landmark=Landmark.WAGON_WHEELS, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-677-car-wheel@3x.png'),
    Jump(length_ft=17, angle=160),
    UnsurveyedLine(length_ft=396, angle=50, include_in_total_surveyed=True),
    SaveLandmark(landmark=Landmark.LISAS_GIFT, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-70-gift@3x.png'),
    UnsurveyedLine(length_ft=50, angle=320, alt_text='', include_in_total_surveyed=True),
    Jump(length_ft=50, angle=140),
    UnsurveyedLine(length_ft=268, angle=70, include_in_total_surveyed=True),
    SaveLandmark(landmark=Landmark.KIBBETTS, icon_path='icons/rowboat.png'),
)

UmbrellaToRockIsland = (
    SurveyedLine(length_ft=18, angle=20),
    Stake(),
    SurveyedLine(length_ft=21, angle=10),
    Stake(),
    SurveyedLine(length_ft=52, angle=20),
    Stake(),
    SurveyedLine(length_ft=25, angle=20),
    Stake(),
    SurveyedLine(length_ft=87, angle=20),
    Stake(),
    SurveyedLine(length_ft=29, angle=10),
    Stake(),
    SurveyedLine(length_ft=27, angle=20),
    Stake(),
    SurveyedLine(length_ft=38, angle=5),
    Stake(),
    SurveyedLine(length_ft=68, angle=10),
    Stake(),
    SurveyedLine(length_ft=27, angle=0),
    TieOff(), # ROCK
    SurveyedLine(length_ft=18, angle=40),
    Stake(),
    SurveyedLine(length_ft=39, angle=0),
    Stake(),
    SurveyedLine(length_ft=35, angle=355),
    Stake(),
    SurveyedLine(length_ft=17, angle=10),
    Stake(),
    SurveyedLine(length_ft=17, angle=0),
    Stake(),
    SurveyedLine(length_ft=23, angle=0),
    Stake(),
    SurveyedLine(length_ft=25, angle=0),
    Stake(),
    SurveyedLine(length_ft=20, angle=10),
    Stake(),
    SurveyedLine(length_ft=20, angle=0),
    Stake(),
    SurveyedLine(length_ft=17, angle=0),
    Stake(),
    SurveyedLine(length_ft=13, angle=0),
    Stake(),
    SurveyedLine(length_ft=23, angle=0),
    Stake(),
    SurveyedLine(length_ft=27, angle=0),
    Stake(),
    SurveyedLine(length_ft=33, length_in=6, angle=348),
    Stake(),
    SurveyedLine(length_ft=23, angle=350),
    Stake(),
    SurveyedLine(length_ft=27, angle=345),
    Stake(),
    SurveyedLine(length_ft=22, angle=310, flip_text_side=True),
    SurveyedLine(length_ft=15, angle=40),
    SaveLandmark(Landmark.ROWBOAT, icon_path='icons/rowboat.png'),
    Jump(length_ft=15, angle=220),
    SurveyedLine(length_ft=15, angle=315, flip_text_side=True),
    Stake(),
    SurveyedLine(length_ft=16, angle=320),
    Stake(),
    SurveyedLine(length_ft=24, angle=330),
    Stake(),
    SurveyedLine(length_ft=22, angle=310),
    Stake(),
    SurveyedLine(length_ft=24, angle=325),
    Stake(),
    SurveyedLine(length_ft=15, angle=325),
    Stake(),
    SurveyedLine(length_ft=15, angle=325),
    Stake(),
    SaveLandmark(Landmark.ROCK_ISLAND_BOTTLE)
    )

UmbrellaToOxygenTanks = (
    SurveyedLine(length_ft=3, angle=340, alt_text=''),
    Stake(zorder=2),
    SurveyedLine(length_ft=49, angle=340),
    Stake(),
    SurveyedLine(length_ft=49, angle=335),
    Stake(),
    SurveyedLine(length_ft=49, angle=320),
    Stake(),
    SurveyedLine(length_ft=13, angle=340),
    TieOff(), # BARREL
    SurveyedLine(length_ft=28, angle=300),
    Stake(),
    SurveyedLine(length_ft=40, angle=280),
    TieOff(), # ROCK1
    SurveyedLine(length_ft=34, angle=35, flip_text_side=True),
    TieOff(), # ROCK2
    SurveyedLine(length_ft=32, angle=40),
    TieOff(), # ROCK3
    SurveyedLine(length_ft=46, angle=280),
    Stake(),
    SurveyedLine(length_ft=35, angle=280),
    Stake(),
    SurveyedLine(length_ft=48, angle=235),
    Stake(),
    SurveyedLine(length_ft=48, angle=240),
    Stake(),
    SurveyedLine(length_ft=24, angle=280),
    SaveLandmark(Landmark.OXYGEN_TANKS, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-256-oxygen-bottles@3x.png'),
)

RockIslandBottleClockwise = (
    SurveyedLine(length_ft=35, angle=225),
    Stake(),
    SurveyedLine(length_ft=54, angle=235),
    Stake(),
    SurveyedLine(length_ft=50, angle=240),
    Stake(),
    SurveyedLine(length_ft=51, angle=240),
    Stake(),
    SurveyedLine(length_ft=53, angle=240),
    Stake(),
    SurveyedLine(length_ft=53, angle=220),
    Stake(),
    SurveyedLine(length_ft=52, angle=220),
    Stake(),
    SurveyedLine(length_ft=52, angle=235),
    Stake(),
    SurveyedLine(length_ft=48, angle=220),
    Stake(),
    SurveyedLine(length_ft=48, angle=250),
    TieOff(),
    SaveLandmark(Landmark.ROCK_ISLAND_T)
    )

RockIslandTClockwise = (
    SurveyedLine(length_ft=72, angle=220),
    TieOff(),
    UnsurveyedLine(length_ft=25, angle=240, alt_text=''),
    )

RockIslandBottleCounterClockwise = (
    UnsurveyedLine(length_ft=50, angle=45, alt_text=''),
    )

PlatformToFourWay = (
    SurveyedLine(length_ft=78, angle=215),
    TieOff(),
    SurveyedLine(length_ft=15, angle=260),
    SurveyedLine(length_ft=57, angle=230),
    TieOff(),
    SurveyedLine(length_ft=63, angle=250),
    TieOff(),
    SurveyedLine(length_ft=10, angle=250, alt_text=''),
    # SurveyedLine(length_ft=73, angle=240, alt_text='83\''),
    SurveyedLine(length_ft=73, angle=240),
    TieOff(),
    SurveyedLine(length_ft=36, angle=222.5, flip_text_side=True),
    TieOff(),
    UnsurveyedLine(length_ft=50, angle=185, alt_text=''),
    Jump(length_ft=50, angle=5),
    SurveyedLine(length_ft=69, angle=270),
    TieOff(),
    SurveyedLine(length_ft=38, angle=245),
    TieOff(),
    SurveyedLine(length_ft=9, angle=250, alt_text=''),
    SurveyedLine(length_ft=63, angle=315),
    TieOff(),
    SurveyedLine(length_ft=42, angle=315, flip_text_side=True),
    SaveLandmark(Landmark.FOUR_WAY),
    )

JJJ = (
    SurveyedLine(length_ft=31, angle=260, flip_text_side=True),
    # WICKER CHAIR TO RIGHT
    SurveyedLine(length_ft=25, angle=240),
    Stake(),
    SurveyedLine(length_ft=24, angle=210, flip_text_side=True),
    TieOff(),
    SurveyedLine(length_ft=20, angle=280),
    TieOff(),
    SurveyedLine(length_ft=58, angle=210),
    TieOff(),
    SurveyedLine(length_ft=83, angle=250),
    TieOff(),
    SurveyedLine(length_ft=20, angle=230),
    Arrow(angle=50, distance=0, color='red'),
    UnsurveyedLine(length_ft=50, angle=300),
    Jump(length_ft=50, angle=120),
    SurveyedLine(length_ft=15, length_in=6, angle=210),
    TieOff(),
    SurveyedLine(length_ft=35, length_in=6, angle=230),
    TieOff(),
    SurveyedLine(length_ft=23, angle=230),
    TieOff(),
    SurveyedLine(length_ft=24, angle=210),
    TieOff(),
    SurveyedLine(length_ft=16, angle=215),
    TieOff(),
    SurveyedLine(length_ft=36, angle=250),
    TieOff(),
    SurveyedLine(length_ft=11, angle=235),
    TieOff(),
    SurveyedLine(length_ft=53, angle=230),
    TieOff(),
    SaveLandmark(Landmark.BYPASS_END_JJJ),
    )

FourWayToNatesTieoff = (
    Arrow(angle=135, distance=0),
    SurveyedLine(length_ft=30, angle=330),
    TieOff(),
    SurveyedLine(length_ft=29, angle=340),
    Stake(),
    UnsurveyedLine(length_ft=150, angle=305, alt_text='Josh\'s deep line', flip_text_side=True),
    Jump(length_ft=150, angle=125),
    SurveyedLine(length_ft=14, angle=325),
    TieOff(),
    SurveyedLine(length_ft=13, length_in=6, angle=320),
    TieOff(),
    SurveyedLine(length_ft=8, angle=330),
    TieOff(),
    SurveyedLine(length_ft=19, length_in=6, angle=315),
    TieOff(),
    SurveyedLine(length_ft=34, angle=330),
    Stake(),
    SurveyedLine(length_ft=59, angle=10),
    SaveLandmark(Landmark.NATES_TIEOFF, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-233-lasso@3x.png'),
    )

NatesTieoffToRockIsland = (
    SurveyedLine(length_ft=109, angle=70),
    Stake(),
    SurveyedLine(length_ft=51, angle=55),
    Stake(),
    SurveyedLine(length_ft=24, angle=55),
    Stake(),
    SurveyedLine(length_ft=104, angle=0),
    Stake(),
    SurveyedLine(length_ft=115, angle=30),
    Stake(),
    UnsurveyedLine(length_ft=50, angle=120),
    Jump(length_ft=50, angle=300),
    SurveyedLine(length_ft=57, angle=25),
    Stake(),
    SurveyedLine(length_ft=33, angle=30),
    Stake(),
    SurveyedLine(length_ft=52, angle=30),
    Stake(),
    SurveyedLine(length_ft=167, angle=40),
    SurveyedLine(length_ft=10, angle=20),
    SurveyedLine(length_ft=9, angle=0),
    SurveyedLine(length_ft=9, angle=340),
    )

FourWayToBypassEndSixtyFoot = (
    SurveyedLine(length_ft=47, angle=305),
    TieOff(),
    SurveyedLine(length_ft=52, angle=300),
    TieOff(),
    SurveyedLine(length_ft=47, angle=265),
    SurveyedLine(length_ft=12, angle=240),
    TieOff(),
    SurveyedLine(length_ft=65, angle=235),
    TieOff(),
    SurveyedLine(length_ft=19, angle=230),
    TieOff(),
    SurveyedLine(length_ft=50, angle=245),
    TieOff(),
    SurveyedLine(length_ft=34, angle=255),
    UnsurveyedLine(length_ft=50, angle=300), # crossover
    Jump(length_ft=100, angle=120),
    UnsurveyedLine(length_ft=50, angle=300),
    SurveyedLine(length_ft=33, angle=255),
    TieOff(),
    SurveyedLine(length_ft=50, angle=230),
    SurveyedLine(length_ft=11, angle=220),
    SurveyedLine(length_ft=3, length_in=6, angle=200),
    SurveyedLine(length_ft=48, angle=160),
    TieOff(),
    SurveyedLine(length_ft=45, angle=210),
    SurveyedLine(length_ft=30, angle=160),
    TieOff(),
    SurveyedLine(length_ft=26, angle=175),
    SaveLandmark(Landmark.BYPASS_END_SIXTY_FOOT),
    )

BypassEndToBobsArrow = (
    SurveyedLine(length_ft=60, angle=250),
    TieOff(),
    SurveyedLine(length_ft=94, angle=230),
    TieOff(),
    SurveyedLine(length_ft=46, angle=220),
    TieOff(),
    SurveyedLine(length_ft=50, angle=220),
    Arrow(distance=0, angle=40),
    SaveLandmark(Landmark.BOBS_ARROW)
    )

BobsArrowToEmmaMunsen = (
    SurveyedLine(length_ft=9, angle=335),
    TieOff(),
    SurveyedLine(length_ft=49, angle=355),
    SurveyedLine(length_ft=22, angle=345),
    Stake(),
    SurveyedLine(length_ft=70, angle=10),
    SurveyedLine(length_ft=65, angle=5),
    SurveyedLine(length_ft=50, angle=5),
    SurveyedLine(length_ft=22, angle=355),
    SaveLandmark(Landmark.EMMA_MUNSEN, icon_path='icons/tugboat.png', zoom=10)
)

BobsArrowToIslander = (
    SurveyedLine(length_ft=25, angle=220),
    TieOff(),
    SurveyedLine(length_ft=104, angle=250),
    TieOff(),
    SurveyedLine(length_ft=12, angle=270),
    TieOff(),
    SurveyedLine(length_ft=25, angle=250),
    SurveyedLine(length_ft=25, angle=245),
    SurveyedLine(length_ft=24, angle=240),
    SurveyedLine(length_ft=22, angle=235),
    SurveyedLine(length_ft=21, angle=230),
    TieOff(),
    SurveyedLine(length_ft=15, angle=185),
    TieOff(),
    SurveyedLine(length_ft=55, angle=205),
    TieOff(),
    SurveyedLine(length_ft=61, angle=205),
    TieOff(),
    SurveyedLine(length_ft=54, angle=200),
    TieOff(),
    UnsurveyedLine(length_ft=50, angle=150),
    )

ExampleData = (
    SaveLandmark(Landmark.MY_BOAT, icon_path='icons/rowboat.png'),
    SurveyedLine(length_ft=100, angle=90),
    Stake(),
    UnsurveyedLine(length_ft=100, angle=45, alt_text='(Unsurveyed line)'),
    Jump(length_ft=100, angle=225),
    SurveyedLine(length_ft=50, length_in=8, angle=135),
    TieOff(),
    SurveyedLine(length_ft=150, angle=100),
    SurveyedLine(length_ft=75, angle=80),
    Stake(),
    UnsurveyedLine(length_ft=25, angle=120, alt_text=''),
    )
