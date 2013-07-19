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

    def _log(self, message):
        if self.debugMode:
            print message

    def fetch_url(self, url, params=None, method=None):

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

        if (method == "DELETE"):
            req.get_method = lambda: 'DELETE'

        response = urllib2.urlopen(req)
        responseObject = json.loads(response.read())

        return responseObject["content"]

    def create_conditions(self, offset, limit, filterArray, order_by):
        params = {}

        if (offset):
            params["offset"] = offset
        if (limit):
            params["limit"] = limit
        if (filterArray):
            params["filter"] = json.dumps(filterArray)
        if (order_by):
            params["order_by"] = order_by

        return params

    def get_user(self):
        return self.fetch_url('/user')

    def get_usage(self):
        path = "/user/usage"
        return self.fetch_url(path)

    def get_forms(self, offset=None, limit=None, filterArray=None, order_by=None):
        params = self.create_conditions(offset, limit, filterArray, order_by)

        path = "/user/forms"

        if (params):
            path = path + "?" + urllib.urlencode(params)

        return self.fetch_url(path)

    def get_submissions(self, offset=None, limit=None, filterArray=None, order_by=None):
        params = self.create_conditions(offset, limit, filterArray, order_by)

        path = "/user/submissions"

        if (params):
            path = path + "?" + urllib.urlencode(params)
            
        return self.fetch_url(path)

    def get_subusers(self):
        path = "/user/subusers"
        return self.fetch_url(path)

    def get_folders(self):
        path = "/user/folders"
        return self.fetch_url(path)

    def get_reports(self):
        path = "/user/reports"
        return self.fetch_url(path)

    def get_settings(self):
        path = "/user/settings"
        return self.fetch_url(path)

    def get_history(self):
        path = "/user/history"
        return self.fetch_url(path)

    def get_form(self, formID):
        return self.fetch_url('/forms/' + formID)

    def get_form_questions(self, formID):
        path = "/form/" + formID + "/questions"
        return self.fetch_url(path)

    def get_form_question(self, formID,  qid):
        path = "/form/" + formID + "/quesiton/" + qid
        return self.fetch_url(path)

    def get_form_submissions(self, formID, offset=None, limit=None, filterArray=None, order_by=None):
        params = self.create_conditions(offset, limit, filterArray, order_by)

        path = "/form/" + formID + "/submissions"

        if (params):
            path = path + "?" + urllib.urlencode(params)

        return self.fetch_url(path)

    def get_form_files(self, formID):
        path = "/form/" + formID + "/files"
        return self.fetch_url(path)

    def create_form_submissions(self, formID, submission):
        sub = {}

        for key in submission.keys():
            if "_" in key:
                sub['submission[' + key[0:key.find("_")] + '][' + key[key.find("_")+1:len(key)] + ']'] = submission[key]
            else:
                sub['submission[' + key + ']'] = submission[key]

        path = "/form/" + formID + "/submissions"
        return self.fetch_url(path, sub)

    def get_form_webhooks(self, formID):
        path = "/form/" + formID + "/webhooks"
        return self.fetch_url(path)

    def create_form_webhook(self, formID, webhookURL):
        path = "/form/" + formID + "/webhooks"
        params = {
            'webhookURL': webhookURL
        }
        return self.fetch_url(path, params)

    def get_submission(self, sid):
        path = "/submission/" + sid
        return self.fetch_url(path)

    def get_report(self, reportID):
        path = "/report/" + reportID
        return self.fetch_url(path)

    def get_folder(self, folderID):
        path = "/folder/" + folderID
        return self.fetch_url(path)

    def get_form_properties(self, formID):
        path = "/form/" + formID + "/properties"
        return self.fetch_url(path)

    def get_form_property(self, formID, propertyKey):
        path = "/form/" + formID + "/properties/" + propertyKey
        return self.fetch_url(path)

    def delete_submission(self, sid):
        path = "/submission/" + sid
        return self.fetch_url(path, None, "DELETE")

    def edit_submission(self, sid, submission):
        sub = {}

        for key in submission.keys():
            if "_" in key:
                sub['submission[' + key[0:key.find("_")] + '][' + key[key.find("_")+1:len(key)] + ']'] = submission[key]
            else:
                sub['submission[' + key + ']'] = submission[key]
                
        path = "/submission/" + sid
        return self.fetch_url(path, sub)

    def clone_form(self, formID):
        params = {"method": "post"}
        path = "/form/" + formID + "/clone"

        return self.fetch_url(path, params)

    def delete_form_question(self, formID, qid):
        path = "/form/" + formID + "/question/" + qid
        return self.fetch_url(path, None, "DELETE")
        