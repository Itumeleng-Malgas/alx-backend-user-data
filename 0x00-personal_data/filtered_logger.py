#!/usr/bin/env python3
""" Obfuscate messages """

from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator:str) -> str:
    """ returns the log message obfuscated """
    return re.sub(r'({})'.format('|'.join(fields)), redaction, message)
