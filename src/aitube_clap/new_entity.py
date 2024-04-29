import uuid
from types import ClapEntity, ClapAssetSource, ClapEntityAudioEngine, ClapEntityGender, ClapEntityRegion, ClapEntityAppearance, ClapSegmentCategory
import random
from helpers.generate_seed import generate_seed

def new_entity(maybe_entity: dict = None):
    if maybe_entity is None:
        maybe_entity = {}

    entity = ClapEntity(
        id=maybe_entity.get('id', str(uuid.uuid4())),
        category=maybe_entity.get('category', ClapSegmentCategory.CHARACTER),
        triggerName=maybe_entity.get('triggerName', ""),
        label=maybe_entity.get('label', ""),
        description=maybe_entity.get('description', ""),
        author=maybe_entity.get('author', ""),
        thumbnailUrl=maybe_entity.get('thumbnailUrl', ""),
        seed=is_valid_number(maybe_entity.get('seed')) and maybe_entity.get('seed') or generate_seed(),
        
        imagePrompt=maybe_entity.get('imagePrompt', ""),
        imageSourceType=maybe_entity.get('imageSourceType', ClapAssetSource.EMPTY),
        imageEngine=maybe_entity.get('imageEngine', ""),
        imageId=maybe_entity.get('imageId', ""),
        audioPrompt=maybe_entity.get('audioPrompt', ""),
        audioSourceType=maybe_entity.get('audioSourceType', ClapAssetSource.EMPTY),
        audioEngine=maybe_entity.get('audioEngine', ClapEntityAudioEngine.PARLER_TTS),
        audioId=maybe_entity.get('audioId', ""),
        
        age=is_valid_number(maybe_entity.get('age')) and maybe_entity.get('age') or 25,
        gender=maybe_entity.get('gender', ClapEntityGender.OBJECT),
        region=maybe_entity.get('region', ClapEntityRegion.GLOBAL),
        appearance=maybe_entity.get('appearance', ClapEntityAppearance.NEUTRAL),
    )

    return entity