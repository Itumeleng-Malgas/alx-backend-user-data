#!/usr/bin/env python3
""" Obfuscate messages """

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Returns the log message obfuscated """
    return re.sub(r'({}=).*?(?={})'.format('|'.join(map(re.escape, fields)),
                  re.escape(separator)), r'\1' + redaction, message)
