#!/usr/bin/python3
import string
print(''.join([getattr(string, '_concat')(getattr(string, 'ascii_uppercase'), '\n')]))
