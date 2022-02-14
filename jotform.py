#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# JotForm API - Python Client
#
# copyright : 2020 JotForm, Inc.
# link : http://www.jotform.com
# version : 1.0
# package : JotFormAPI

import urllib.request, urllib.parse, urllib.error
import json

class JotformAPIClient:
    DEFAULT_BASE_URL = 'https://api.jotform.com/'
    EU_BASE_URL = 'https://eu-api.jotform.com/'

    __apiVersion = 'v1'

    __apiKey = None
    __debugMode = False
    __outputType = "json"

    def __init__(self, apiKey='', baseUrl=DEFAULT_BASE_URL, outputType='json', debug=False):
        self.__apiKey = apiKey
        self.__baseUrl = baseUrl
        self.__outputType = outputType.lower()
        self.__debugMode = debug

    def _log(self, message):
        if self.__debugMode:
            print(message)

    def set_baseurl(self, baseurl):
        self.__baseUrl = baseurl

    def get_debugMode(self):
        return self.__debugMode
    def set_debugMode(self, value):
        self.__debugMode = value

    def get_outputType(self):
        return self.__outputType
    def set_outputType(self, value):
        self.__outputType = value

    def fetch_url(self, url, params=None, method=None):
        if(self.__outputType != 'json'):
            url = url + '.xml'

        url = self.__baseUrl + self.__apiVersion + url

        self._log('fetching url ' + url)
        if (params):
            self._log(params)

        headers = {
            'apiKey': self.__apiKey
        }

        if (method == 'GET'):
            if (params):
                url = url + '?' + urllib.parse.urlencode(params)

            req = urllib.request.Request(url, headers=headers, data=None)
        elif (method == 'POST'):
            if (params):
                data = urllib.parse.urlencode(params).encode('utf-8')
            else:
                data = None
            req = urllib.request.Request(url, headers=headers, data=data)
        elif (method == 'DELETE'):
            req = urllib.request.Request(url, headers=headers, data=None)
            req.get_method = lambda: 'DELETE'
        elif (method == 'PUT'):
            if (params):
                params = params.encode("utf-8")
            req = urllib.request.Request(url, headers=headers, data=params)
            req.get_method = lambda: 'PUT'

        response = urllib.request.urlopen(req)

        if (self.__outputType == 'json'):
            responseObject = json.loads(response.read().decode('utf-8'))
            return responseObject['content']
        else:
            data = response.read()
            response.close()
            return data

    def create_conditions(self, offset, limit, filterArray, order_by):
        args = {'offset': offset, 'limit': limit, 'filter': filterArray, 'orderby': order_by}
        params = {}

        for key in list(args.keys()):
            if(args[key]):
                if(key == 'filter'):
                    params[key] = json.dumps(args[key])
                else:
                    params[key] = args[key]

        return params

    def create_history_query(self, action, date, sortBy, startDate, endDate):
        args = {'action': action, 'date': date, 'sortBy': sortBy, 'startDate': startDate, 'endDate': endDate}
        params = {}

        for key in list(args.keys()):
            if (args[key]):
                params[key] = args[key]

        return params

    def get_user(self):
        """Get user account details for a JotForm user.

        Returns:
            User account type, avatar URL, name, email, website URL and account limits.
        """

        return self.fetch_url('/user', method='GET')

    def get_usage(self):
        """Get number of form submissions received this month.

        Returns:
            Number of submissions, number of SSL form submissions, payment form submissions and upload space used by user.
        """

        return self.fetch_url('/user/usage', method='GET')

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

        return self.fetch_url('/user/forms', params, 'GET')

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

        return self.fetch_url('/user/submissions', params, 'GET')

    def get_subusers(self):
        """Get a list of sub users for this account.

        Returns:
            List of forms and form folders with access privileges.
        """

        return self.fetch_url('/user/subusers', method='GET')

    def get_folders(self):
        """Get a list of form folders for this account.

        Returns:
            Name of the folder and owner of the folder for shared folders.
        """

        return self.fetch_url('/user/folders', method='GET')

    def get_reports(self):
        """List of URLS for reports in this account.

        Returns:
            Reports for all of the forms. ie. Excel, CSV, printable charts, embeddable HTML tables.
        """

        return self.fetch_url('/user/reports', method='GET')

    def get_settings(self):
        """Get user's settings for this account.

        Returns:
            User's time zone and language.
        """

        return self.fetch_url('/user/settings', method='GET')

    def update_settings(self, settings):
        """Update user's settings.

        Args:
            settings (array): New user setting values with setting keys

        Returns:
            Changes on user settings.
        """

        return self.fetch_url('/user/settings', settings, 'POST')

    def get_history(self, action=None, date=None, sortBy=None, startDate=None, endDate=None):
        """Get user activity log.

        Args:
            action (enum): Filter results by activity performed. Default is 'all'.
            date (enum): Limit results by a date range. If you'd like to limit results by specific dates you can use startDate and endDate fields instead.
            sortBy (enum): Lists results by ascending and descending order.
            startDate (string): Limit results to only after a specific date. Format: MM/DD/YYYY.
            endDate (string): Limit results to only before a specific date. Format: MM/DD/YYYY.

        Returns:
            Activity log about things like forms created/modified/deleted, account logins and other operations.
        """

        params = self.create_history_query(action, date, sortBy, startDate, endDate)

        return self.fetch_url('/user/history', params, 'GET')

    def get_form(self, formID):
        """Get basic information about a form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            Form ID, status, update and creation dates, submission count etc.
        """

        return self.fetch_url('/form/' + formID, method='GET')

    def get_form_questions(self, formID):
        """Get a list of all questions on a form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            Question properties of a form.
        """

        return self.fetch_url('/form/' + formID + '/questions', method='GET')

    def get_form_question(self, formID,  qid):
        """Get details about a question

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            qid (string): Identifier for each question on a form. You can get a list of question IDs from /form/{id}/questions.

        Returns:
            Question properties like required and validation.
        """
        return self.fetch_url('/form/' + formID + '/question/' + qid, method='GET')

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

        return self.fetch_url('/form/' + formID + '/submissions', params, 'GET')

    def create_form_submission(self, formID, submission):
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

        return self.fetch_url('/form/' + formID + '/submissions', sub, 'POST')

    def create_form_submissions(self, formID, submissions):
        """Submit data to this form using the API.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            submission (json): Submission data with question IDs.

        Returns:
            Posted submission ID and URL.
        """

        return self.fetch_url('/form/' + formID + '/submissions', submissions, 'PUT')

    def get_form_files(self, formID):
        """List of files uploaded on a form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            Uploaded file information and URLs on a specific form.
        """

        return self.fetch_url('/form/' + formID + '/files', method='GET')

    def get_form_webhooks(self, formID):
        """Get list of webhooks for a form

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            List of webhooks for a specific form.
        """

        return self.fetch_url('/form/' + formID + '/webhooks', method='GET')

    def create_form_webhook(self, formID, webhookURL):
        """Add a new webhook

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            webhookURL (string): Webhook URL is where form data will be posted when form is submitted.

        Returns:
            List of webhooks for a specific form.
        """

        params = {'webhookURL': webhookURL}

        return self.fetch_url('/form/' + formID + '/webhooks', params, 'POST')

    def delete_form_webhook(self, formID, webhookID):
        """Delete a specific webhook of a form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            webhookID (string): You can get webhook IDs when you call /form/{formID}/webhooks.

        Returns:
            Remaining webhook URLs of form.
        """

        return self.fetch_url('/form/' + formID + '/webhooks/' + webhookID, None, 'DELETE')

    def get_submission(self, sid):
        """Get submission data

        Args:
            sid (string): You can get submission IDs when you call /form/{id}/submissions.

        Returns:
            Information and answers of a specific submission.
        """

        return self.fetch_url('/submission/' + sid, method='GET')

    def get_report(self, reportID):
        """Get report details

        Args:
            reportID (string): You can get a list of reports from /user/reports.

        Returns:
            Properties of a speceific report like fields and status.
        """

        return self.fetch_url('/report/' + reportID, method='GET')

    def get_folder(self, folderID):
        """Get folder details

        Args:
            folderID (string): Get a list of folders from /user/folders

        Returns:
            A list of forms in a folder, and other details about the form such as folder color.
        """

        return self.fetch_url('/folder/' + folderID, method='GET')

    def create_folder(self, folderProperties):
        """ Create a new folder

        Args:
            folderProperties (array): Properties of new folder.

        Returns:
            New folder.
        """

        return self.fetch_url('/folder', folderProperties, 'POST')

    def delete_folder(self, folderID):
        """Delete a specific folder and its subfolders

        Args:
            folderID (string): You can get a list of folders and its subfolders from /user/folders.

        Returns:
            Status of request.
        """

        return self.fetch_url('/folder/' + folderID, None, 'DELETE')

    def update_folder(self, folderID, folderProperties):
        """Update a specific folder

        Args:
            folderID (string): You can get a list of folders and its subfolders from /user/folders.
            folderProperties (json): New properties of the specified folder.

        Returns:
            Status of request.
        """

        return self.fetch_url('/folder/' + folderID, folderProperties, 'PUT')

    def add_forms_to_folder(self, folderID, formIDs):
        """Add forms to a folder

        Args:
            folderID (string): You can get the list of folders and its subfolders from /user/folders.
            formIDs (array): You can get the list of forms from /user/forms.

        Returns:
            Status of request.
        """

        formattedFormIDs = json.dumps({"forms": formIDs})
        return self.update_folder(folderID, formattedFormIDs)

    def add_form_to_folder(self, folderID, formID):
        """Add a specific form to a folder

        Args:
            folderID (string): You can get the list of folders and its subfolders from /user/folders.
            formID (string): You can get the list of forms from /user/forms.

        Returns:
            Status of request.
        """

        formattedFormID = json.dumps({"forms": [formID]})
        return self.update_folder(folderID, formattedFormID)

    def get_form_properties(self, formID):
        """Get a list of all properties on a form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            Form properties like width, expiration date, style etc.
        """

        return self.fetch_url('/form/' + formID + '/properties', method='GET')

    def get_form_property(self, formID, propertyKey):
        """Get a specific property of the form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            propertyKey (string): You can get property keys when you call /form/{id}/properties.

        Returns:
            Given property key value.
        """

        return self.fetch_url('/form/' + formID + '/properties/' + propertyKey, method='GET')

    def get_form_reports(self, formID):
        """Get all the reports of a form, such as excel, csv, grid, html, etc.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            List of all reports in a form, and other details about the reports such as title.
        """

        return self.fetch_url('/form/' + formID + '/reports', method='GET')

    def create_report(self, formID, report):
        """Create new report of a form

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            report (array): Report details. List type, title etc.

        Returns:
            Report details and URL
        """
        return self.fetch_url('/form/' + formID + '/reports', report, 'POST')

    def delete_submission(self, sid):
        """Delete a single submission.

        Args:
            sid (string): You can get submission IDs when you call /form/{id}/submissions.

        Returns:
            Status of request.
        """

        return self.fetch_url('/submission/' + sid, None, 'DELETE')

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
            if '_' in key and key != "created_at":
                sub['submission[' + key[0:key.find('_')] + '][' + key[key.find('_')+1:len(key)] + ']'] = submission[key]
            else:
                sub['submission[' + key + ']'] = submission[key]

        return self.fetch_url('/submission/' + sid, sub, 'POST')

    def clone_form(self, formID):
        """Clone a single form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            Status of request.
        """
        params = {"method": "post"}

        return self.fetch_url('/form/' + formID + '/clone', params, 'POST')

    def delete_form_question(self, formID, qid):
        """Delete a single form question.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            qid (string): Identifier for each question on a form. You can get a list of question IDs from /form/{id}/questions.

        Returns:
            Status of request.
        """

        return self.fetch_url('/form/' + formID + '/question/' + qid, None, 'DELETE')

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

        return self.fetch_url('/form/' + formID + '/questions', params, 'POST')

    def create_form_questions(self, formID, questions):
        """Add new questions to specified form.

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            questions (json): New question properties like type and text.

        Returns:
            Properties of new question.
        """

        return self.fetch_url('/form/' + formID + '/questions', questions, 'PUT')

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

        return self.fetch_url('/form/' + formID + '/question/' + qid, question, 'POST')

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

        return self.fetch_url('/form/' + formID + '/properties', properties, 'POST')

    def set_multiple_form_properties(self, formID, form_properties):
        """Add or edit properties of a specific form

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
            form_properties (json): New properties like label width.

        Returns:
            Edited properties.
        """

        return self.fetch_url('/form/' + formID + '/properties', form_properties, 'PUT')

    def create_form(self, form):
        """ Create a new form

        Args:
            form (array): Questions, properties and emails of new form.

        Returns:
            New form.
        """

        params = {}

        for key in form.keys():
            value = form[key]
            for k in value.keys():
                if (key == 'properties'):
                    for k in value.keys():
                        params[key + '[' + k + ']'] = value[k]
                else:
                    v = value[k]
                    for a in v.keys():
                        params[key + '[' + k + '][' + a + ']'] =v[a]

        return self.fetch_url('/user/forms', params, 'POST')

    def create_forms(self, form):
        """ Create new forms

        Args:
            form (json): Questions, properties and emails of forms.

        Returns:
            New forms.
        """

        return self.fetch_url('/user/forms', form, 'PUT')

    def delete_form(self, formID):
        """Delete a specific form

        Args:
            formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.

        Returns:
            Properties of deleted form.
        """

        return self.fetch_url('/form/' + formID, None, 'DELETE')

    def register_user(self, userDetails):
        """Register with username, password and email

        Args:
            userDetails (array): Username, password and email to register a new user

        Returns:
            New user's details
        """

        return self.fetch_url('/user/register', userDetails, 'POST')

    def login_user(self, credentials):
        """Login user with given credentials

        Args:
            credentials (array): Username, password, application name and access type of user

        Returns:
            Logged in user's settings and app key
        """

        return self.fetch_url('/user/login', credentials, 'POST')

    def logout_user(self):
        """Logout user

        Returns:
            Status of request
        """

        return self.fetch_url('/user/logout', method='GET')

    def get_plan(self, plan_name):
        """Get details of a plan

        Args:
            plan_name (string): Name of the requested plan. FREE, PREMIUM etc.

        Returns:
            Details of a plan
        """

        return self.fetch_url('/system/plan/' + plan_name, method='GET')

    def delete_report(self, reportID):
        """Delete a specific report

        Args:
            reportID (string): You can get a list of reports from /user/reports.

        Returns:
            Status of request.
        """

        return self.fetch_url('/report/' + reportID, None, 'DELETE')
