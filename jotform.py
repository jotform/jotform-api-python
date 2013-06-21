#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Jotform API Wrapper
# copyright : Interlogy LLC
#
__author__ = "canerbalci@gmail.com (Caner Balci)"

import urllib
import urllib2
import json


class JotformAPIClient:

    def __init__(self, apiKey, debug=False, outputType="json"):

        self.baseUrl = "http://api.jotform.com/"
        self.apiVersion = "v1"
        self.apiKey = apiKey
        self.debugMode = debug
        self.outputType = outputType
        self.user = self.get_user()
        self.username = self.user["username"]

    def _log(self, message):
        if self.debugMode:
            print message

    def fetch_url(self, url, params=None):

        url = self.baseUrl + self.apiVersion + url
        self._log('fetching url ' + url)

        headers = {
            'apiKey': self.apiKey
        }

        if (params):
            data = urllib.urlencode(params)
        else:
            data = None

        req = urllib2.Request(url, headers=headers, data=data)
        response = urllib2.urlopen(req)
        responseObject = json.loads(response.read())

        return responseObject["content"]

    def get_user(self):
        return self.fetch_url('/user')

    def get_usage(self):
        path = "/user/" + self.username + "/usage"
        return self.fetch_url(path)

    def get_forms(self):
        return self.fetch_url('/user/forms')

    def get_submissions(self):
        path = "/user/" + self.username + "/submissions"
        return self.fetch_url(path)

    def get_subusers(self):
        path = "/user/" + self.username + "/subusers"
        return self.fetch_url(path)

    def get_folders(self):
        path = "/user/" + self.username + "/folders"
        return self.fetch_url(path)

    def get_reports(self):
        path = "/user/" + self.username + "/reports"
        return self.fetch_url(path)

    def get_settings(self):
        path = "/user/" + self.username + "/settings"
        return self.fetch_url(path)

    def get_history(self):
        path = "/user/" + self.username + "/history"
        return self.fetch_url(path)

    def get_form(self, formID):
        return self.fetch_url('/forms/' + formID)

    def get_form_questions(self, formID):
        path = "/form/" + formID + "/questions"
        return self.fetch_url(path)

    def get_form_question(self, formID,  qid):
        path = "/form/" + formID + "/quesiton/" + qid
        return self.fetch_url(path)

    def get_form_submissions(self, formID):
        path = "/form/" + formID + "/submissions"
        return self.fetch_url(path)

    def get_form_files(self, formID):
        path = "/form/" + formID + "/files"
        return self.fetch_url(path)

    def create_form_submission(self, formID, submission):
        path = "/form/" + formID + "/submissions"
        return self.fetch_url(path, submission)

    def get_form_webhooks(self, formID):
        path = "/form/" + formID + "/webhooks"
        return self.fetch_url(path)

    def create_form_webhook(self, formID, webhookURL):
        path = "/form/" + formID + "/webhooks"
        params = {
            'webhookURL': webookURL
        }
        return self.fetch_url(path, params)

    def get_submission(self, sid):
        path = "/submission/" + sid
        return self.fetch_url(path)

    def get_report(self, reportID):
        path = "/report/" + reportID
        return self.fetch_url(path)

    def get_folder(self, folderID):
        path = "/folder/" + self.folderID
        return self.fetch_url(path)
        