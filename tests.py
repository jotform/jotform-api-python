#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Jotform API Wrapper :: Tests
# copyright : Interlogy LLC
#

from jotform import *


def main():
    print 'tests are running'

    jotti = JotformAPIClient('', True)

    print jotti.username
    print jotti.user['id']

if __name__ == "__main__":
    main()
