"""
 Created by qujl on 2018-08-01
"""
__author__ = 'qujl'

import xmltodict
import json


def xml2json(_str):
    """
        demo Python xml to json
    """
    try:
        _dict = xmltodict.parse(_str)
        return json.dumps(_dict)
    except Exception:
        return None