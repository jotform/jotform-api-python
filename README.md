jotform-api-python 
===============
[JotForm API](http://api.jotform.com/docs/) - Python Client


### Installation

Install via git clone:

        $ git clone https://github.com/jotform/jotform-api-python.git
        $ cd jotform-api-python
        
Install via pip (latest version)

        $ pip install git+https://github.com/jotform/jotform-api-python.git

### Documentation

You can find the docs for the API of this client at [http://api.jotform.com/docs/](http://api.jotform.com/docs). Argument names and descriptions can be found in jotform.py.

### Authentication

JotForm API requires API key for all user related calls. You can create your API Keys at  [API section](http://www.jotform.com/myaccount/api) of My Account page.

### Examples

Print all forms of the user

```python
from jotform import *

def main():

    jotformAPIClient = JotformAPIClient('YOUR API KEY')

    forms = jotformAPIClient.get_forms()
    # get_forms Args:
    #     offset (string): Start of each result set for form list. (optional)
    #     limit (string): Number of results in each result set for form list. (optional)
    #     filterArray (array): Filters the query results to fetch a specific form range.(optional)
    #     order_by (string): Order results by a form field name. (optional)
    for form in forms:
    	print(form["title"])

if __name__ == "__main__":
    main()
```  

Get submissions of the latest form

```python
from jotform import *

def main():

    jotformAPIClient = JotformAPIClient('YOUR API KEY')

    forms = jotformAPIClient.get_forms(offset=None, limit=1, filterArray=None, order_by=None)
    # get_forms Args:
    #     offset (string): Start of each result set for form list. (optional)
    #     limit (string): Number of results in each result set for form list. (optional)
    #     filterArray (array): Filters the query results to fetch a specific form range.(optional)
    #     order_by (string): Order results by a form field name. (optional)
    latestForm = forms[0]

    latestFormID = latestForm["id"]

    submissions = jotformAPIClient.get_form_submissions(formID=latestFormID)
    # get_form_submissions Args:
    #     formID (string): Form ID is the numbers you see on a form URL. You can get form IDs when you call /user/forms.
    #     offset (string): Start of each result set for form list. (optional)
    #     limit (string): Number of results in each result set for form list. (optional)
    #     filterArray (array): Filters the query results to fetch a specific form range.(optional)
    #     order_by (string): Order results by a form field name. (optional)
    print(submissions)

if __name__ == "__main__":
    main()
``` 

Get latest 100 submissions ordered by creation date

```python
from jotform import *

def main():

    jotformAPIClient = JotformAPIClient('YOUR API KEY')

    submissions = jotformAPIClient.get_submissions(offset=0, limit=100, filterArray=None, order_by="created_at")
    # get_submissions Args:
    #         offset (string): Start of each result set for form list. (optional)
    #         limit (string): Number of results in each result set for form list. (optional)
    #         filterArray (array): Filters the query results to fetch a specific form range.(optional)
    #         order_by (string): Order results by a form field name. (optional)

    print(submissions)

if __name__ == "__main__":
    main()
``` 

Submission and form filter examples

```python
from jotform import *

def main():

    jotformAPIClient = JotformAPIClient('YOUR API KEY')

    submission_filter = {"id:gt":"FORM ID", "created_at": "DATE"}

    submission = jotformAPIClient.get_submissions(offset=0, limit=0, filterArray=submission_filter, order_by="")
    # get_submissions Args:
    #         offset (string): Start of each result set for form list. (optional)
    #         limit (string): Number of results in each result set for form list. (optional)
    #         filterArray (array): Filters the query results to fetch a specific form range.(optional)
    #         order_by (string): Order results by a form field name. (optional)
    print(submission)

    form_filter = {"id:gt": "FORM ID"}

    forms = jotformAPIClient.get_forms(offset=0, limit=0, filterArray=form_filter, order_by="")
    # get_forms Args:
    #     offset (string): Start of each result set for form list. (optional)
    #     limit (string): Number of results in each result set for form list. (optional)
    #     filterArray (array): Filters the query results to fetch a specific form range.(optional)
    #     order_by (string): Order results by a form field name. (optional)
    print(forms)

if __name__ == "__main__":
    main()
``` 

Delete last 50 submissions

```python
from jotform import *

def main():

    jotformAPIClient = JotformAPIClient('YOUR API KEY')

    submissions = jotformAPIClient.get_submissions(offset=0, limit=50, filterArray=None, order_by=None)
    # get_submissions Args:
    #         offset (string): Start of each result set for form list. (optional)
    #         limit (string): Number of results in each result set for form list. (optional)
    #         filterArray (array): Filters the query results to fetch a specific form range.(optional)
    #         order_by (string): Order results by a form field name. (optional)
    for submission in submissions:
        result = jotformAPIClient.delete_submission(sid=submission["id"])
    # delete_submission Args:
    #     sid (string): You can get submission IDs when you call /form/{id}/submissions.
        print(result)

if __name__ == "__main__":
    main()
``` 

First the _JotformAPIClient_ class is included from the _jotform-api-python/jotform.py_ file. This class provides access to JotForm's API. You have to create an API client instance with your API key. 
In case of an exception (wrong authentication etc.), you can catch it or let it fail with a fatal error.
