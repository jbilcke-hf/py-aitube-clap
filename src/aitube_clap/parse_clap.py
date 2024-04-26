import yaml
import gzip
import requests
from io import BytesIO
from typing import Union
from uuid import uuid4
from types import (ClapProject, ClapHeader, ClapMeta, ClapModel, ClapScene, ClapSegment,
                   ClapSceneEvent, ClapSegmentCategory, ClapOutputType, ClapSegmentStatus,
                   ClapAuthor)

def parse_clap(source: Union[ClapProject, str, bytes], debug: bool = False) -> ClapProject:
    if isinstance(source, ClapProject):
        if debug:
            print("parse: Input is already a Clap project.")
        return source
    
    input_data = None

    if isinstance(source, str):
        if source.startswith(("http://", "https://")):
            if debug:
                print("parse: Input is a remote URL.")
            response = requests.get(source)
            input_data = response.content
        elif source.startswith(("data:application/x-gzip;base64,", "data:application/octet-stream;base64,")):
            if debug:
                print("parse: Input is a base64 encoded data URI.")
            base64_encoded_data = source.split(',', 1)[1]
            input_data = base64.b64decode(base64_encoded_data)
        else:
            if debug:
                print("parse: Input is a YAML string.")
            input_data = source.encode()
    elif isinstance(source, bytes):
        input_data = source
    
    if input_data.startswith(b'\x1f\x8b'):
        if debug:
            print("parse: Input data is compressed with gzip.")
        decompressed_data = gzip.decompress(input_data)
        loaded_data = yaml.safe_load(decompressed_data)
    else:
        loaded_data = yaml.safe_load(input_data)

    if debug:
        print("parse: YAML data loaded, converting to ClapProject.")
    return convert_to_clap_project(loaded_data, debug)

def convert_to_clap_project(data: dict, debug: bool = False) -> ClapProject:
    # Extract header and meta first
    clap_header = ClapHeader(**data[0])
    clap_meta = ClapMeta(**data[1])
    
    models, scenes, segments = [], [], []

    index_offset = 2  # Because first two entries are header and meta

    model_entries = data[index_offset:index_offset+clap_header.numberOfModels]
    scene_entries = data[index_offset+clap_header.numberOfModels:index_offset+clap_header.numberOfModels+clap_header.numberOfScenes]
    segment_entries = data[index_offset+clap_header.numberOfModels+clap_header.numberOfScenes:]

    for model in model_entries:
        models.append(ClapModel(**model))
    for scene in scene_entries:
        events = [ClapSceneEvent(**event) for event in scene.get('events', [])]
        scenes.append(ClapScene(**scene, events=events))
    for segment in segment_entries:
        segments.append(ClapSegment(**segment))

    if debug:
        print(f"parse: Parsed {len(models)} models, {len(scenes)} scenes, {len(segments)} segments.")

    return ClapProject(meta=clap_meta, models=models, scenes=scenes, segments=segments)