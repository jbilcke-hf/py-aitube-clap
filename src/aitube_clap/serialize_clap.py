import yaml
import gzip
from types import ClapProject

def serialize_clap(project: ClapProject) -> bytes:
    clap_data = yaml.dump(project.__dict__)
    gzip_data = gzip.compress(clap_data.encode())
    return gzip_data