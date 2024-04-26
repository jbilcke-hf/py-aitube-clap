import requests
from parse_clap import parse_clap
from types import ClapProject

def fetch_clap(url: str, options: dict = None) -> ClapProject:
    if options is None:
        options = {}
    
    method = options.get("method", "GET")
    headers = options.get("headers", {})
    data = options.get("body", None)  # In requests, 'body' should be provided as 'data' or 'json'
    cache = options.get("cache", None)  # Python 'requests' does not support 'cache', handled via session if needed

    response = requests.request(method, url, headers=headers, data=data)
    
    if response.status_code == 200:
        # In Python, we directly use the content of the response.
        # Assuming content comes gzip-compressed similar to what we've handled in parse_clap.
        clap_project = parse_clap(response.content)
        return clap_project
    else:
        raise Exception(f"Failed to fetch: {response.status_code}")
