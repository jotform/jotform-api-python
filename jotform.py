#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Jotform API Wrapper
# copyright : Interlogy LLC
#

__author__ = "canerbalci@gmail.com (Caner Balci)"

from urllib2 import Request, urlopen, URLError, HTTPError
import json


class JotformAPIClient:

    def __init__(self, apiKey, debug=False, outputType="json"):
        
        self.baseUrl = "http://www.jotform.com/API/"
        self.apiVersion = "v1"

        self.apiKey = apiKey
        self.debugMode = debug
        self.outputType = outputType

        self.user = getUser()
        self.username = self.user.username



    def fetchUrl(self, url, params):

        url = self.baseUrl + self.apiVersion + url

        user_agent = "Jotform Python API Client v1"
        headers = {'User-Agent': user_agent}

        params['apiKey'] = self.apiKey

        data = urllib.urlencode(params)
        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req)
        resp = response.read()

        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
        else:
            # everything is fine

    def getUser(self):
        return self.fetchUrl('/user')
