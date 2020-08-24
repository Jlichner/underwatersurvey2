from dataclasses import dataclass
from enum import Enum

#####
#
# Surveyers:
#
#   Ben Rother
#   Brian Chu
#   Christian Lundkvist
#   Doug Dwyer
#   Jamie Lichner
#   JP Vanier
#   Lisa Goodlin
#   Mike Burr
#   Scott Fuller
#   Stephanie Yang
#
#####

class Landmark(Enum):
    BAR = 0
    CAR = 1
    CONROY = 2
    FOUR_WAY = 3
    ISLANDER_T = 4
    KIBBETTS = 5
    LISAS_GIFT = 6
    MOORING_BLOCK_20FT = 7
    MY_BOAT = 8 # For the README
    OXYGEN_TANKS = 9
    ROCK_ISLAND_T = 10
    ROWBOAT = 11
    SKELETON = 12
    UMBRELLA = 13
    WAGON_WHEELS = 14
    NATES_TIEOFF = 15
    BYPASS_END_SIXTY_FOOT = 16
    BYPASS_END_JJJ = 17
    ROCK_ISLAND_BOTTLE = 18
    BOBS_ARROW = 19
    EMMA_MUNSEN = 20
    ANCHOR = 21
    MOORING_BLOCK_1 = 24
    MOORING_BLOCK_2 = 25
    MOORING_BLOCK_3 = 26
    MOORING_BLOCK_4 = 27
    MOORING_BLOCK_5 = 28
    # Mooring block 6 is the same as the skeleton
    ANGLE_IRON = 29
    WRECK_1 = 30
    STEAM_ENGINE = 31
    BOAT_RAMP_1=32
    BOAT_RAMP_2=33
    WRECK_2 = 34
    WRECK_3 = 35
    TRACTOR_TIRE = 36

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

@dataclass(frozen=True)
class RemovedLine(AbstractLine):
    color: str = 'lightgrey'
    linestyle: str = 'solid'

@dataclass(frozen=True)
class MarinaLine(AbstractLine):
    color: str = 'red' 
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
    zorder: int = 3
    transparent_icon: bool = False

@dataclass(frozen=True)
class Stake:
    color: str = 'brown' 
    marker: str = 's'
    zorder: int = 2
    text: str = None
    text_rotation: int = 0

@dataclass(frozen=True)
class RemovedStake(Stake):
    color: str = 'lightgrey' 
    marker: str = 's'

@dataclass(frozen=True)
class TieOff:
    color: str = 'blue' 
    marker: str = 'h'
    zorder: int = 3
    force_draw: bool = False

@dataclass(frozen=True)
class Arrow:
    distance: int = 10 # default for home arrows
    angle: int = 0.0
    color: str = 'white'

BarToPlatform = (
    TieOff(force_draw=True),
    SurveyedLine(length_ft=23, angle=330),
    # TieOff(), Line change
    SurveyedLine(length_ft=36, length_in=8, angle=330),
    Arrow(distance=8, angle=150),
    # TieOff(), JP's tent
    SurveyedLine(length_in=9, angle=325),
    SaveLandmark(Landmark.MOORING_BLOCK_20FT, icon_path='icons/mooringblock.png', transparent_icon=True),
    SurveyedLine(length_ft=44, length_in=8, angle=310),
    SaveLandmark(Landmark.SKELETON, icon_path='icons/mooringblock.png', transparent_icon=True),
    )

SkeletonToMooringBlock2ViaPokerRun = (
    SurveyedLine(length_ft=47, length_in=9, angle=60),
    SurveyedLine(length_ft=40, angle=55),
    TieOff(),
    SurveyedLine(length_ft=72, angle=50),
    TieOff(force_draw=True),
    SaveLandmark(Landmark.BOAT_RAMP_1),
    MarinaLine(length_ft=35, length_in=10, angle=60),
    SaveLandmark(Landmark.BOAT_RAMP_2),
    TieOff(force_draw=True),
    SurveyedLine(length_ft=20, length_in=8, angle=50),
    Jump(length_ft=8, angle=315),
    SaveLandmark(landmark=Landmark.CAR, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-6-car@3x.png'),
    Jump(length_ft=100, angle=90),  # NOTE(stpyang): This is a hack to extend the small maps
    Jump(length_ft=100, angle=270), # NOTE(stpyang): This is a hack to extend the small maps
    Jump(length_ft=8, angle=315),
    SurveyedLine(length_ft=19, length_in=7, angle=300),
    TieOff(),
    SurveyedLine(length_ft=54, length_in=6, angle=300),
    SaveLandmark(landmark=Landmark.UMBRELLA, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-14-beach-umbrella@3x.png'),
    SurveyedLine(length_ft=4, length_in=8, angle=240),
    # Stake(),
    SurveyedLine(length_ft=51, length_in=10, angle=240),
    Stake(),
    SurveyedLine(length_ft=50, angle=235),
    Stake(),
    SurveyedLine(length_ft=43, length_in=11, angle=240),
    SaveLandmark(landmark=Landmark.ANCHOR, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-258-anchor@3x.png'),
    SurveyedLine(length_ft=47, length_in=10, angle=175),
    Stake(),
    SurveyedLine(length_ft=15, length_in=2, angle=175),
    SaveLandmark(landmark=Landmark.MOORING_BLOCK_2, icon_path='icons/mooringblock.png', transparent_icon=True),
    )

SkeletonToMooringBlock2ViaMooringBlocks = (
    Jump(length_ft=22, length_in=1, angle=335),
    SaveLandmark(landmark=Landmark.MOORING_BLOCK_4, icon_path='icons/mooringblock.png', transparent_icon=True),
    Jump(length_ft=21, length_in=7, angle=325),
    )

MooringBlock2ToMooringBlock1 = (
    Jump(length_ft=25, length_in=9, angle=230),
    SaveLandmark(Landmark.MOORING_BLOCK_1, icon_path='icons/mooringblock.png', transparent_icon=True),
    )

MooringBlock1ToMooringBlock5ViaPokerRun = (
    SurveyedLine(length_ft=64, length_in=9, angle=280),
    TieOff(),
    SurveyedLine(length_ft=14, length_in=11, angle=222),
    Jump(length_ft=6, length_in=4, angle=200),
    SaveLandmark(landmark=Landmark.CONROY, icon_path='icons/conroy.png'),
    Jump(length_ft=100, angle=270),  # NOTE(stpyang): This is a hack to extend the small maps
    Jump(length_ft=100, angle=90),   # NOTE(stpyang): This is a hack to extend the small maps
    Jump(length_ft=6, length_in=4, angle=200),
    SurveyedLine(length_ft=49, length_in=2, angle=160),
    TieOff(),
    SaveLandmark(Landmark.ANGLE_IRON),
    SurveyedLine(length_ft=65, length_in=10, angle=75),
    TieOff(),
    SurveyedLine(length_ft=12, length_in=1, angle=75),
    SurveyedLine(length_ft=6, length_in=6, angle=100),
    SaveLandmark(landmark=Landmark.MOORING_BLOCK_5, icon_path='icons/mooringblock.png', transparent_icon=True),
)

MooringBlock1ToMooringBlock5ViaMooringBlocks = (
    Jump(length_ft=21, length_in=2, angle=140),
    SaveLandmark(landmark=Landmark.MOORING_BLOCK_3, icon_path='icons/mooringblock.png', transparent_icon=True),
    Jump(length_ft=25, length_in=10, angle=145),
)

CarToLisasGift = (
    SurveyedLine(length_ft=38, length_in=6, angle=56),
    Stake(),
    SurveyedLine(length_ft=27, angle=56),
    TieOff(),
    SurveyedLine(length_ft=34, angle=46),
    Stake(),
    SurveyedLine(length_ft=19, length_in=10, angle=46),
    TieOff(),
    SurveyedLine(length_ft=13, length_in=2, angle=37),
    Stake(),
    SurveyedLine(length_ft=3, angle=58),
    TieOff(),
    SurveyedLine(length_ft=10, angle=58),
    Stake(), # loose
    SurveyedLine(length_ft=22, angle=58),
    SurveyedLine(length_ft=20, length_in=7, angle=27),
    Stake(),
    SurveyedLine(length_ft=57, length_in=4, angle=48),
    Stake(),
    SurveyedLine(length_ft=22, angle=50),
    Stake(),
    SurveyedLine(length_ft=50, angle=52),
    Stake(),
    SurveyedLine(length_ft=27, angle=332),
    SaveLandmark(landmark=Landmark.WAGON_WHEELS, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-677-car-wheel@3x.png'),
    Jump(length_ft=27, angle=152),
    SurveyedLine(length_ft=28, angle=50),
    Stake(),
    SurveyedLine(length_ft=22, length_in=4, angle=50),
    Stake(),
    SurveyedLine(length_ft=28, angle=50),
    Stake(),
    SurveyedLine(length_ft=22, angle=42),
    Stake(),
    SurveyedLine(length_ft=28, angle=48),
    Stake(),
    SurveyedLine(length_ft=21, length_in=10, angle=54),
    Stake(),
    SurveyedLine(length_ft=28, angle=54),
    Stake(),
    SurveyedLine(length_ft=22, angle=54),
    Stake(),
    SurveyedLine(length_ft=28, length_in=6, angle=54),
    Stake(),
    SurveyedLine(length_ft=21, length_in=6, angle=54),
    Stake(),
    SurveyedLine(length_ft=42, angle=54),
    SaveLandmark(landmark=Landmark.LISAS_GIFT, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-70-gift@3x.png'),
    Jump(length_ft=100, angle=90),  # NOTE(stpyang): This is a hack to extend the small maps
    Jump(length_ft=100, angle=270),   # NOTE(stpyang): This is a hack to extend the small maps
)

CarToLisasGiftTruncated = (
    UnsurveyedLine(length_ft=50, angle=56),
)

LisasGiftToWreck1 = (
    SurveyedLine(length_ft=50, angle=322),
    Stake(),
    SurveyedLine(length_ft=43, length_in=7, angle=325),
    Stake(),
    SurveyedLine(length_ft=42, length_in=6, angle=330),
    # Stake(),
    SaveLandmark(landmark=Landmark.WRECK_1, icon_path='icons/shipwreck.png'), # 21 feet long
)

Wreck1ToWreck2 = (
    UnsurveyedLine(length_ft=344, angle=66, include_in_total_surveyed=False),
)

LisasGiftNortheast = (
    SurveyedLine(length_ft=50, length_in=5, angle=72),
    Stake(),
    SurveyedLine(length_ft=50, length_in=4, angle=72),
    Stake(),
    SurveyedLine(length_ft=49, length_in=3, angle=70),
    Stake(),
    SurveyedLine(length_ft=50, length_in=1, angle=71),
    Stake(),
    SurveyedLine(length_ft=50, length_in=1, angle=66),
    Stake(),
    SurveyedLine(length_ft=34, length_in=6, angle=76),
    Stake(),
    Jump(length_ft=18, length_in=10, angle=140), # gap
    SaveLandmark(landmark=Landmark.KIBBETTS, icon_path='icons/shipwreck.png'),
    Jump(length_ft=6, length_in=10, angle=140),
    Jump(length_ft=6, length_in=10, angle=140),
    TieOff(),
    SurveyedLine(length_ft=60, length_in=2, angle=60),
    Stake(),
    UnsurveyedLine(length_ft=50, angle=60),
    Jump(length_ft=50, angle=240),
    Arrow(angle=240),
    SurveyedLine(length_ft=80, length_in=6, angle=334),
    SurveyedLine(length_ft=20, length_in=3, angle=334),
    SurveyedLine(length_ft=28, angle=314),
    TieOff(),
    SurveyedLine(length_ft=54, length_in=8, angle=314),
    Jump(length_ft=8, angle=350),
    SaveLandmark(landmark=Landmark.WRECK_2, icon_path='icons/shipwreck.png'),
    # Jump(length_ft=8, angle=170),
    RemovedLine(length_ft=40, length_in=7, angle=262),
    # TieOff(),
    RemovedLine(length_ft=61, angle=256),
    RemovedLine(length_ft=35, length_in=6, angle=326),
    RemovedLine(length_ft=12, angle=342),
    RemovedLine(length_ft=60, angle=20),
    RemovedLine(length_ft=57, length_in=8, angle=44),
    Stake(),
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
    SaveLandmark(Landmark.ROWBOAT, icon_path='icons/shipwreck.png'),
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
    SurveyedLine(length_ft=3, angle=335, alt_text=''),
    # Stake(),
    SurveyedLine(length_ft=49, length_in=6, angle=335),
    Stake(),
    SurveyedLine(length_ft=49, length_in=4, angle=330),
    Stake(),
    SurveyedLine(length_ft=49, angle=335),
    Stake(),
    SurveyedLine(length_ft=19, length_in=10, angle=320),
    TieOff(), # BARREL
    SurveyedLine(length_ft=29, angle=310),
    Stake(),
    SurveyedLine(length_ft=42, length_in=1, angle=300),
    Stake(),
    SurveyedLine(length_ft=41, angle=290),
    Stake(),
    SurveyedLine(length_ft=32, length_in=1, angle=280),
    Stake(),
    SurveyedLine(length_ft=32, length_in=6, angle=280),
    Stake(),
    SurveyedLine(length_ft=27, angle=280),
    SaveLandmark(Landmark.OXYGEN_TANKS, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-256-oxygen-bottles@3x.png'),
)

UmbrellaToOxygenTanksTruncated = (
    UnsurveyedLine(length_ft=25, angle=335),
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

AngleIronToFourWay = (
    SurveyedLine(length_ft=78, angle=222),
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
    SaveLandmark(Landmark.EMMA_MUNSEN, icon_path='icons/tugboat.png')
)

BobsArrowToIslander = (
    SurveyedLine(length_ft=25, angle=220),
    TieOff(),
    SurveyedLine(length_ft=104, angle=250),
    TieOff(),
    SurveyedLine(length_ft=16, length_in=5, angle=270),
    TieOff(),
    SurveyedLine(length_ft=23, angle=270),
    SurveyedLine(length_ft=23, angle=250),
    SurveyedLine(length_ft=35, angle=235),
    SurveyedLine(length_ft=35, angle=225),
    TieOff(),
    SurveyedLine(length_ft=14, angle=195),
    TieOff(),
    SurveyedLine(length_ft=54, angle=210),
    TieOff(),
    SurveyedLine(length_ft=60, angle=210),
    TieOff(),
    SurveyedLine(length_ft=58, angle=200),
    TieOff(),
    SurveyedLine(length_ft=54, angle=150),
    SaveLandmark(Landmark.TRACTOR_TIRE, icon_path='glyphicons-pro/glyphicons-basic-2-3/png/glyphicons-basic-137-cogwheel@3x.png'),
    UnsurveyedLine(length_ft=47, length_in=6, angle=120),
    # TieOff(), # LOG PILE BEGIN
    # Jump(length_ft=8, length_in=5, angle=280),
    # UnsurveyedLine(length_ft=6, angle=262),
    # UnsurveyedLine(length_ft=10, length_in=3, angle=216),
    # TieOff(), # END LOGS
    # UnsurveyedLine(length_ft=105, length_in=2, angle=220),
    # TieOff(),
    # UnsurveyedLine(length_ft=39, angle=200),
    # UnsurveyedLine(length_ft=42, angle=205),
    # TieOff(),
    # UnsurveyedLine(length_ft=55, length_in=2, angle=240),
    # TieOff(),
    # UnsurveyedLine(length_ft=10, length_in=5, angle=260),
    # TieOff(),
    # UnsurveyedLine(length_ft=50, angle=260),
)
    

ExampleData = (
    SaveLandmark(Landmark.MY_BOAT, icon_path='icons/shipwreck.png'),
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
