#!/usr/bin/python3


import asyncio
import logging
import re
import sys
import typing
import io
import urllib.error
import urllib.parse

import aiofiles
import aiohttp
from aiohttp import ClientSession


logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)

logger = logging.getLogger('areq')
logging.getLogger("chardet.charsetprober").disabled = True

HREF_RE = re.compile(r'href="(.*?)"')

async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    # GET request wrapper to fetch page HTML
    # Kwards are passed to 'session.request()'
    resp = await session.request(method="GET", url=url, **kwargs)
    resp.raise_for_status()
    logger.info("got response [%s] for URL: %s", resp.status, url)
    html = await resp.text()
    return html









