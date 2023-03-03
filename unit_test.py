from main import *
from constants import *

def test_initial_crawl_sanity():
    if not INITIAL_CRAWL:
       assert not initial_crawl()
    initial_crawl()