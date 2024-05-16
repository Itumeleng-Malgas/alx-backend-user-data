#!/usr/bin/env python3
""" Obfuscate messages """
import re


def filter_datum(fields, redaction, message, separator):
    """ returns the log message obfuscated """
    return re.sub(r'({})'.format('|'.join(fields)), redaction, message)
