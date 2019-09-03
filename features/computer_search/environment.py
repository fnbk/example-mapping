# -*- coding: UTF-8 -*-

import logging
logging.basicConfig(format='%(message)s')

# ----------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ----------------------------------------------------------------------------
from behave import register_type
import json

def parse_ids(ids):
    # logging.warning(type(ids))
    # logging.warning(ids)
    strippedIds = ids.strip('\'"') 
    strIds = json.loads(strippedIds)
    strIds = list(map(lambda x: int(x), strIds))
    return strIds

# -- REGISTER: User-defined type converter (parse_type).
register_type(IdList=parse_ids)