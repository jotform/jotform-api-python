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

    def executePutRequest(self, url, params):
        url = self.baseUrl + self.apiVersion + url

        headers = {
            'apiKey': self.apiKey
        }

        req = urllib2.Request(url, headers=headers, data=params)
        req.get_method = lambda: 'PUT'

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
        """Get user account details for a JotForm user.

        Returns:
            User account type, avatar URL, name, email, website URL and account limits.
        """

        return self.fetch_url('/user')

    def get_usage(self):
        """Get number of form submissions received this month.

        Returns:
            Number of submissions, number of SSL form submissions, payment form submissions and upload space used by user.
        """
        
        path = "/user/usage"
        return self.fetch_url(path)

    def get_forms(self, offset=None, limit=None, filterArray=None, order_by=None):
        """Get a list of forms for this account

        Args:
            offset (string): Start of each result set for form list. (optional)
            limit (string): Number of results in each result set for form list. (optional)
            filterArray (array): Filters the query results to fetch a specific form range.(optional)
            order_by (string): Order results by a form field name. (optional)

        Returns:
            Basic details such as title of the form, when it was created, number of new and total submissions.
        """

        params = self.create_conditions(offset, limit, filterArray, order_by)

        path = "/user/forms"

        if (params):
            path = path + "?" + urllib.urlencode(params)

        return self.fetch_url(path)

    def get_submissions(self, offset=None, limit=None, filterArray=None, order_by=None):
        """Get a list of submissions for this account.

        Args:
            offset (string): Start of each result set for form list. (optional)
            limit (string): Number of results in each result set for form list. (optional)
            filterArray (array): Filters the query results to fetch a specific form range.(optional)
            order_by (string): Order results by a form field name. (optional)

        Returns:
            Basic details such as title of the form, when it was created, number of new and total submissions.
        """

        params = self.create_conditions(offset, limit, filterArray, order_by)

        path = "/user/submissions"

        if (params):
            path = path + "?" + urllib.urlencode(params)
            
        return self.fetch_url(path)

    def get_subusers(self):
        """Get a list of sub users for this account.

        Returns:
            List of forms and form folders with access privileges.
        """

        path = "/user/subusers"
        return self.fetch_url(path)

    def get_folders(self):
        """Get a list of form folders for this account.

        Returns:
            Name of the folder and owner of the folder for shared folders.
        """

        path = "/user/folders"
        return self.fetch_url(path)

    def get_reports(self):
        """List of URLS for reports in this account.

        Returns:
            Reports for all of the forms. ie. Excel, CSV, printable charts, embeddable HTML tables.
        """

        path = "/user/reports"
        return self.fetch_url(path)

    def get_settings(self):
        """Get user's settings for this account.

        Returns:
            User's time zone and language.
        """
        
        path = "/user/settings"
        return self.fetch_url(path)

    def get_history(self):
        """Get user activity log.

        Returns:
            Activity log about things like forms created/modified/deleted, account logins and other operations.
        """

        path = "/user/history"
        return self.fetch_url(path)

    def get_form(self, formID):
        """Get basic information about a form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            Form ID, status, update and creation dates, submission count etc.
        """

        return self.fetch_url('/forms/' + formID)

    def get_form_questions(self, formID):
        """Get a list of all questions on a form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            Question properties of a form.
        """

        path = "/form/" + formID + "/questions"
        return self.fetch_url(path)

    def get_form_question(self, formID,  qid):
        """Get details about a question

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            qid (string): Identifier for each question on a form. You can get a list of question IDs from /form/{id}/questions.

        Returns:
            Question properties like required and validation.
        """

        path = "/form/" + formID + "/quesiton/" + qid
        return self.fetch_url(path)

    def get_form_submissions(self, formID, offset=None, limit=None, filterArray=None, order_by=None):
        """List of a form submissions.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            offset (string): Start of each result set for form list. (optional)
            limit (string): Number of results in each result set for form list. (optional)
            filterArray (array): Filters the query results to fetch a specific form range.(optional)
            order_by (string): Order results by a form field name. (optional)

        Returns:
            Submissions of a specific form.
        """

        params = self.create_conditions(offset, limit, filterArray, order_by)

        path = "/form/" + formID + "/submissions"

        if (params):
            path = path + "?" + urllib.urlencode(params)

        return self.fetch_url(path)

    def create_form_submissions(self, formID, submission):
        """Submit data to this form using the API.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            submission (array): Submission data with question IDs.

        Returns:
            Posted submission ID and URL.
        """

        sub = {}

        for key in submission.keys():
            if "_" in key:
                sub['submission[' + key[0:key.find("_")] + '][' + key[key.find("_")+1:len(key)] + ']'] = submission[key]
            else:
                sub['submission[' + key + ']'] = submission[key]

        path = "/form/" + formID + "/submissions"
        return self.fetch_url(path, sub)

    def get_form_files(self, formID):
        """List of files uploaded on a form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            Uploaded file information and URLs on a specific form.
        """

        path = "/form/" + formID + "/files"
        return self.fetch_url(path)

    def get_form_webhooks(self, formID):
        """Get list of webhooks for a form

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            List of webhooks for a specific form.
        """

        path = "/form/" + formID + "/webhooks"
        return self.fetch_url(path)

    def create_form_webhook(self, formID, webhookURL):
        """Add a new webhook

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            webhookURL (string): Webhook URL is where form data will be posted when form is submitted. 

        Returns:
            List of webhooks for a specific form.
        """

        path = "/form/" + formID + "/webhooks"
        params = {
            'webhookURL': webhookURL
        }
        return self.fetch_url(path, params)

    def get_submission(self, sid):
        """Get submission data

        Args:
            sid (string): You can get submission IDs when you call /form/{id}/submissions.

        Returns:
            Information and answers of a specific submission.
        """

        path = "/submission/" + sid
        return self.fetch_url(path)

    def get_report(self, reportID):
        """Get report details

        Args:
            reportID (string): You can get a list of reports from /user/reports.

        Returns:
            Properties of a speceific report like fields and status.
        """

        path = "/report/" + reportID
        return self.fetch_url(path)

    def get_folder(self, folderID):
        """Get folder details

        Args:
            folderID (string): Get a list of folders from /user/folders

        Returns:
            A list of forms in a folder, and other details about the form such as folder color.
        """

        path = "/folder/" + folderID
        return self.fetch_url(path)

    def get_form_properties(self, formID):
        """Get a list of all properties on a form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            Form properties like width, expiration date, style etc.
        """

        path = "/form/" + formID + "/properties"
        return self.fetch_url(path)

    def get_form_property(self, formID, propertyKey):
        """Get a specific property of the form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            propertyKey (string): You can get property keys when you call /form/{id}/properties.

        Returns:
            Given property key value.
        """

        path = "/form/" + formID + "/properties/" + propertyKey
        return self.fetch_url(path)

    def delete_submission(self, sid):
        """Delete a single submission.

        Args:
            sid (string): You can get submission IDs when you call /form/{id}/submissions.

        Returns:
            Status of request.
        """

        path = "/submission/" + sid
        return self.fetch_url(path, None, "DELETE")

    def edit_submission(self, sid, submission):
        """Edit a single submission.

        Args:
            sid (string): You can get submission IDs when you call /form/{id}/submissions.
            submission (array): New submission data with question IDs.

        Returns:
            Status of request.
        """

        sub = {}

        for key in submission.keys():
            if "_" in key:
                sub['submission[' + key[0:key.find("_")] + '][' + key[key.find("_")+1:len(key)] + ']'] = submission[key]
            else:
                sub['submission[' + key + ']'] = submission[key]
                
        path = "/submission/" + sid
        return self.fetch_url(path, sub)

    def clone_form(self, formID):
        """Clone a single form.
        
        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            Status of request.
        """
        params = {"method": "post"}
        path = "/form/" + formID + "/clone"

        return self.fetch_url(path, params)

    def delete_form_question(self, formID, qid):
        """Delete a single form question.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            qid (string): Identifier for each question on a form. You can get a list of question IDs from /form/{id}/questions.

        Returns:
            Status of request.
        """

        path = "/form/" + formID + "/question/" + qid
        return self.fetch_url(path, None, "DELETE")

    def create_form_question(self, formID, question):
        """Add new question to specified form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            question (array): New question properties like type and text.

        Returns:
            Properties of new question.
        """
        params = {}

        for key in question.keys():
            params['question[' + key + ']'] = question[key]

        path = "/form/" + formID + "/questions"
        return self.fetch_url(path, params)

    def create_form_questions(self, formID, questions):
        """Add new questions to specified form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            questions (json): New question properties like type and text.

        Returns:
            Properties of new question.
        """
        path = "/form/" + formID + "/questions"
        return self.executePutRequest(path, questions)

    def edit_form_question(self, formID, qid, question_properties):
        """Add or edit a single question properties.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            qid (string): Identifier for each question on a form. You can get a list of question IDs from /form/{id}/questions.
            question_properties (array): New question properties like type and text.

        Returns:
            Edited property and type of question.
        """
        question = {}

        for key in question_properties.keys():
            question['question[' + key + ']'] = question_properties[key]

        path = "/form/" + formID + "/question/" + qid
        return self.fetch_url(path, question)

    def set_form_properties(self, formID, form_properties):
        """Add or edit properties of a specific form

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            form_properties (array): New properties like label width.

        Returns:
            Edited properties.
        """
        properties = {}

        for key in form_properties.keys():
            properties['properties[' + key + ']'] = form_properties[key]

        path = "/form/" + formID + "/properties"
        return self.fetch_url(path, properties)

    def set_multiple_form_properties(self, formID, form_properties):
        """Add or edit properties of a specific form

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            form_properties (json): New properties like label width.

        Returns:
            Edited properties.
        """
        path = "/form/" + formID + "/properties"
        return self.executePutRequest(path, form_properties)

    def create_form(self, form):
        """ Create a new form

        Args:
            form (json): Questions, properties and emails of new form.

        Returns:
            New form.
        """
        path = "/user/forms"
        return self.executePutRequest(path, form)

    def delete_form(self, formID):
        """Delete a specific form

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            Properties of deleted form.
        """
        path = "/form/" + formID
        return self.fetch_url(path, None, "DELETE")



        