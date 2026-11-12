from __future__ import annotations
def run(url):
 from urllib.parse import urlsplit
 return (urlsplit(url).hostname or "").lower()
