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
        self.user = self.getUser()
        self.username = self.user["username"]

    def _log(self, message):
        if self.debugMode:
            print message

    def fetchUrl(self, url, params=None):
        
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

    def getUser(self):
        return self.fetchUrl('/user')[0]

    def getForms(self):
        return self.fetchUrl('/user/forms')

    def getFormById(self, formId):
        return self.fetchUrl('/forms/' + formId)

    def getFormById(self, formId):
        path = "/form/" + formId
        return self.fetchUrl(path)

    def getQuestionById(self, formId,  questionId):
        path = "/form/" + formId + "/quesiton/" + questionId
        return self.fetchUrl(path)

    def getSubmissionsByFormId(self, formId):
        path = "/form/" + formId + "/submissions"
        return self.fetchUrl(path)

    def getFilesByFormId(self, formId):
        path = "/form/" + formId + "/files"
        return self.fetchUrl(path)

    def getQuestionsByFormId(self, formId):
        path = "/form/" + formId + "/questions"
        return self.fetchUrl(path)

    def deleteQuestionById(self, formId,  questionId):
        path = "/form/" + formId + "\/question\/" + questionId + "/delete"
        return self.fetchUrl(path)

    def deleteQuestionsByFormId(self, formId):
        path = "/form/" + formId + "/question/all/delete"
        return self.fetchUrl(path)

    def getSubmissions(self):
        path = "/user/" + self.username + "/submissions"
        return self.fetchUrl(path)

    def getUserSettings(self):
        path = "/user/" + self.username + "/settings"
        return self.fetchUrl(path)

    def getUserUsage(self):
        path = "/user/" + self.username + "/usage"
        return self.fetchUrl(path)

    def getUserRewards(self):
        path = "/user/" + self.username + "/rewards"
        return self.fetchUrl(path)

    def getUserFolders(self):
        path = "/user/" + self.username + "/folders"
        return self.fetchUrl(path)

    def getUserHistory(self):
        path = "/user/" + self.username + "/history"
        return self.fetchUrl(path)

    def getUserSettingsBySettingKey(self, settingKey):
        path = "/user/" + self.username + "\/settings\/" + settingKey
        return self.fetchUrl(path)

    def getUserSubmissionById(self, subId):
        path = "/user/" + self.username + "\/submission\/" + subId
        return self.fetchUrl(path)

    def getUserInvoices(self):
        path = "/user/" + self.username + "/invoices"
        return self.fetchUrl(path)

    def getRewardTypes(self):
        path = "/system/reward_types"
        return self.fetchUrl(path)

    def getUserKeys(self):
        path = "/user/" + self.username + "/keys"
        return self.fetchUrl(path)

    def getUserApps(self):
        path = "/user/" + self.username + "/apps"
        return self.fetchUrl(path)

    def getUserSubusers(self):
        path = "/user/" + self.username + "/subusers"
        return self.fetchUrl(path)

    def getUserReports(self):
        path = "/user/" + self.username + "/reports"
        return self.fetchUrl(path)

    def getUserReportById(self, reportId):
        path = "/user/" + self.username + "\/report\/" + reportId
        return self.fetchUrl(path)

    def getAvatarList(self):
        path = "/system/avatar_list"
        return self.fetchUrl(path)

    def getPlans(self):
        path = "/system/plans"
        return self.fetchUrl(path)

    def getUserCreditCardChangeLink(self):
        path = "/user/" + self.username + "/payment/creditCardChangeLink"
        return self.fetchUrl(path)

    def getUserGetMoreStatus(self):
        path = "/user/" + self.username + "/getmore/status"
        return self.fetchUrl(path)

    def deleteUserAppKey(self, appKey):
        path = '/user/apps/' + appKey + '/delete'
        return self.fetchUrl(path,  appKey)

    def deleteUserApiKey(self, apiKey):
        path = '/user/keys/' + apiKey + '/delete'
        return self.fetchUrl(path,  apiKey)

    def updateUserKeys(self):
        path = '/user/keys'
        return self.fetchUrl(path)

    def updateUserApiKey(self, apiKey):
        path = '/user/keys' + apiKey
        return self.fetchUrl(path,  apiKey)

    def updateSubusers(self, options):
        path = '/user/subusers/update'
        return self.fetchUrl(path,  options)

    def deleteSubuser(self, options):
        path = '/user/subusers/delete'
        return self.fetchUrl(path,  options)

    def updateUserSubusers(self, options):
        path = '/user/subusers/update'
        return self.fetchUrl(path,  options)

    def updateUserSettings(self, attributes):
        path = '/user/settings'
        return self.fetchUrl(path, attributes)

