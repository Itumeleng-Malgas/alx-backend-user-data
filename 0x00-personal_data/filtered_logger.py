#!/usr/bin/env python3
""" Returns the log message obfuscated """
import re


def filter_datum(fields, redaction, message, separator):
    return re.sub(r'({})'.format('|'.join(fields)), redaction, message)
