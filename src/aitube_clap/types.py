from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

class ClapSegmentCategory(Enum):
    SPLAT = "splat"
    MESH = "mesh"
    DEPTH = "depth"
    EVENT = "event"
    INTERFACE = "interface"
    PHENOMENON = "phenomenon"
    VIDEO = "video"
    STORYBOARD = "storyboard"
    TRANSITION = "transition"
    CHARACTER = "character"
    LOCATION = "location"
    TIME = "time"
    ERA = "era"
    LIGHTING = "lighting"
    WEATHER = "weather"
    ACTION = "action"
    MUSIC = "music"
    SOUND = "sound"
    DIALOGUE = "dialogue"
    STYLE = "style"
    CAMERA = "camera"
    GENERIC = "generic"

class ClapOutputType(Enum):
    TEXT = "text"
    ANIMATION = "animation"
    INTERFACE = "interface"
    EVENT = "event"
    PHENOMENON = "phenomenon"
    TRANSITION = "transition"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"

class ClapSegmentStatus(Enum):
    TO_GENERATE = "to_generate"
    TO_INTERPOLATE = "to_interpolate"
    TO_UPSCALE = "to_upscale"
    COMPLETED = "completed"
    ERROR = "error"

class ClapAuthor(Enum):
    AUTO = "auto"
    AI = "ai"
    HUMAN = "human"

class ClapAssetSource(Enum):
    REMOTE = "REMOTE"
    PATH = "PATH"
    DATA = "DATA"
    PROMPT = "PROMPT"
    EMPTY = "EMPTY"

class ClapEntityGender(Enum):
    MALE = "male"
    FEMALE = "female"
    PERSON = "person"
    OBJECT = "object"

class ClapEntityAppearance(Enum):
    SERIOUS = "serious"
    NEUTRAL = "neutral"
    FRIENDLY = "friendly"
    CHILL = "chill"

class ClapEntityRegion(Enum):
    GLOBAL = "global"
    AMERICAN = "american"
    EUROPEAN = "european"
    BRITISH = "british"
    AUSTRALIAN = "australian"
    CANADIAN = "canadian"
    INDIAN = "indian"
    FRENCH = "french"
    ITALIAN = "italian"
    GERMAN = "german"
    CHINESE = "chinese"

class ClapEntityTimbre(Enum):
    HIGH = "high"
    NEUTRAL = "neutral"
    DEEP = "deep"

class ClapEntityAudioEngine(Enum):
    ELEVEN_LABS = "ElevenLabs"
    XTTS = "XTTS"
    PARLER_TTS = "Parler-TTS"

@dataclass
class ClapVoice:
    name: str
    gender: ClapEntityGender
    age: int
    region: ClapEntityRegion
    timbre: ClapEntityTimbre
    appearance: ClapEntityAppearance
    audioEngine: ClapEntityAudioEngine
    audioId: str

@dataclass
class ClapHeader:
    format: str
    numberOfEntities: int
    numberOfScenes: int
    numberOfSegments: int

@dataclass
class ClapMeta:
    id: str
    title: str
    description: str
    synopsis: str
    licence: str
    orientation: str
    durationInMs: int
    width: int
    height: int
    defaultVideoModel: str
    extraPositivePrompt: List[str]
    screenplay: str
    isLoop: bool
    isInteractive: bool

@dataclass
class ClapSceneEvent:
    id: str
    type: str
    character: Optional[str]
    description: str
    behavior: str
    startAtLine: int
    endAtLine: int

@dataclass
class ClapScene:
    id: str
    scene: str
    line: str
    rawLine: str
    sequenceFullText: str
    sequenceStartAtLine: int
    sequenceEndAtLine: int
    startAtLine: int
    endAtLine: int
    events: List[ClapSceneEvent]

@dataclass
class ClapSegment:
    id: str
    track: int
    startTimeInMs: int
    endTimeInMs: int
    category: ClapSegmentCategory
    entityId: str
    sceneId: str
    prompt: str
    label: str
    outputType: ClapOutputType
    renderId: str
    status: ClapSegmentStatus
    assetUrl: str
    assetDurationInMs: int
    assetSourceType: ClapAssetSource
    createdBy: ClapAuthor
    editedBy: ClapAuthor
    outputGain: float
    seed: int

@dataclass
class ClapEntity:
    id: str
    category: ClapSegmentCategory
    triggerName: str
    label: str
    description: str
    author: str
    thumbnailUrl: str
    seed: int
    imagePrompt: str
    imageSourceType: ClapAssetSource
    imageEngine: str
    imageId: str
    audioPrompt: str
    audioSourceType: ClapAssetSource
    audioEngine: ClapEntityAudioEngine
    audioId: str
    age: int
    gender: ClapEntityGender
    region: ClapEntityRegion
    appearance: ClapEntityAppearance

@dataclass
class ClapProject:
    meta: ClapMeta
    entities: List[ClapEntity]
    scenes: List[ClapScene]
    segments: List[ClapSegment]