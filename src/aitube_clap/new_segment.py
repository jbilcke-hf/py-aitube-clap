import uuid
from types import ClapSegment, ClapSegmentCategory, ClapOutputType, ClapSegmentStatus, ClapAuthor, ClapAssetSource
from helpers.is_valid_number import is_valid_number
from helpers.generate_seed import generate_seed

def new_segment(maybe_segment=None):
    if maybe_segment is None:
        maybe_segment = {}

    # Validate and set up defaults
    start_time_in_ms = maybe_segment.get('startTimeInMs', 0) if is_valid_number(maybe_segment.get('startTimeInMs')) else 0
    asset_duration_in_ms = maybe_segment.get('assetDurationInMs', 1000) if is_valid_number(maybe_segment.get('assetDurationInMs')) else 1000
    end_time_in_ms = maybe_segment.get('endTimeInMs', start_time_in_ms + asset_duration_in_ms) if is_valid_number(maybe_segment.get('endTimeInMs')) else start_time_in_ms + asset_duration_in_ms

    segment = ClapSegment(
        id=maybe_segment.get('id', str(uuid.uuid4())),
        track=maybe_segment.get('track', 0) if is_valid_number(maybe_segment.get('track')) else 0,
        startTimeInMs=start_time_in_ms,
        endTimeInMs=end_time_in_ms,
        category=maybe_segment.get('category', ClapSegmentCategory.GENERIC),
        entityId=maybe_segment.get('entityId', ""),
        sceneId=maybe_segment.get('sceneId', ""),
        prompt=maybe_segment.get('prompt', ""),
        label=maybe_segment.get('label', ""),
        outputType=maybe_segment.get('outputType', ClapOutputType.TEXT),
        renderId=maybe_segment.get('renderId', ""),
        status=maybe_segment.get('status', ClapSegmentStatus.TO_GENERATE),
        assetUrl=maybe_segment.get('assetUrl', ""),
        assetDurationInMs=asset_duration_in_ms,
        assetSourceType=maybe_segment.get('assetSourceType', ClapAssetSource.EMPTY),
        createdBy=maybe_segment.get('createdBy', ClapAuthor.AI),
        editedBy=maybe_segment.get('editedBy', ClapAuthor.AI),
        outputGain=maybe_segment.get('outputGain', 0) if is_valid_number(maybe_segment.get('outputGain')) else 0.0,
        seed=maybe_segment.get('seed', generate_seed()) if is_valid_number(maybe_segment.get('seed')) else generate_seed()
    )

    return segment