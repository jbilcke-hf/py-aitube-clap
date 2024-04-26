
import uuid
from types import ClapMeta, ClapModel, ClapProject, ClapScene, ClapSegment
from helpers.get_valid_number import get_valid_number

def new_clap(clap=None):
    if clap is None:
        clap = {}

    meta_data = clap.get('meta', {})
    models = clap.get('models', [])
    scenes = clap.get('scenes', [])
    segments = clap.get('segments', [])

    meta = ClapMeta(
        id=str(meta_data.get('id', uuid.uuid4())),
        title=meta_data.get('title', ""),
        description=meta_data.get('description', ""),
        synopsis=meta_data.get('synopsis', ""),
        licence=meta_data.get('licence', ""),
        orientation=meta_data.get('orientation', "landscape"),
        durationInMs=get_valid_number(meta_data.get('durationInMs'), 1000, 2**31 - 1, 4000),
        width=get_valid_number(meta_data.get('width'), 256, 8192, 1024),
        height=get_valid_number(meta_data.get('height'), 256, 8192, 576),
        defaultVideoModel=meta_data.get('defaultVideoModel', "SVD"),
        extraPositivePrompt=meta_data.get('extraPositivePrompt', []),
        screenplay=meta_data.get('screenplay', ""),
        isLoop=meta_data.get('isLoop', False),
        isInteractive=meta_data.get('isInteractive', False),
    )

    return ClapProject(
        meta=meta,
        models=models,
        scenes=scenes,
        segments=segments
    )
