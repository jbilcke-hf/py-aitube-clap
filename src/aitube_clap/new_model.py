import uuid
from types import ClapModel, ClapAssetSource, ClapModelAudioEngine, ClapModelGender, ClapModelRegion, ClapModelAppearance, ClapSegmentCategory
import random
from helpers.generate_seed import generate_seed

def new_model(maybe_model: dict = None):
    if maybe_model is None:
        maybe_model = {}

    model = ClapModel(
        id=maybe_model.get('id', str(uuid.uuid4())),
        category=maybe_model.get('category', ClapSegmentCategory.CHARACTER),
        triggerName=maybe_model.get('triggerName', ""),
        label=maybe_model.get('label', ""),
        description=maybe_model.get('description', ""),
        author=maybe_model.get('author', ""),
        thumbnailUrl=maybe_model.get('thumbnailUrl', ""),
        seed=is_valid_number(maybe_model.get('seed')) and maybe_model.get('seed') or generate_seed(),
        
        imagePrompt=maybe_model.get('imagePrompt', ""),
        imageSourceType=maybe_model.get('imageSourceType', ClapAssetSource.EMPTY),
        imageEngine=maybe_model.get('imageEngine', ""),
        imageId=maybe_model.get('imageId', ""),
        audioPrompt=maybe_model.get('audioPrompt', ""),
        audioSourceType=maybe_model.get('audioSourceType', ClapAssetSource.EMPTY),
        audioEngine=maybe_model.get('audioEngine', ClapModelAudioEngine.PARLER_TTS),
        audioId=maybe_model.get('audioId', ""),
        
        age=is_valid_number(maybe_model.get('age')) and maybe_model.get('age') or 25,
        gender=maybe_model.get('gender', ClapModelGender.OBJECT),
        region=maybe_model.get('region', ClapModelRegion.GLOBAL),
        appearance=maybe_model.get('appearance', ClapModelAppearance.NEUTRAL),
    )

    return model