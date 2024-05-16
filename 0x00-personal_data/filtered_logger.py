#!/usr/bin/env python3

def filter_datum(fields, redaction, message, separator):
    import re; return re.sub(r'({})'.format('|'.join(fields)), redaction, message)
