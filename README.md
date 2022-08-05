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

You can find the docs for the API of this client at [http://api.jotform.com/docs/](http://api.jotform.com/docs)

### Authentication

JotForm API requires API key for all user related calls. You can create your API Keys at  [API section](http://www.jotform.com/myaccount/api) of My Account page.

### Examples

Print all forms of the user

```python
from jotform import *

def main():

    jotformAPIClient = JotformAPIClient('YOUR API KEY')

    forms = jotformAPIClient.get_forms()

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

    forms = jotformAPIClient.get_forms(None, 1, None, None)

    latestForm = forms[0]

    latestFormID = latestForm["id"]

    submissions = jotformAPIClient.get_form_submissions(latestFormID)

    print(submissions)

if __name__ == "__main__":
    main()
``` 

Get latest 100 submissions ordered by creation date

```python
from jotform import *

def main():

    jotformAPIClient = JotformAPIClient('YOUR API KEY')

    submissions = jotformAPIClient.get_submissions(0, 100, None, "created_at")

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

    submission = jotformAPIClient.get_submissions(0, 0, submission_filter, "") 
    print(submission)

    form_filter = {"id:gt": "FORM ID"}

    forms = jotformAPIClient.get_forms(0,0, form_filter, "")
    print(forms)

if __name__ == "__main__":
    main()
``` 

Delete last 50 submissions

```python
from jotform import *

def main():

    jotformAPIClient = JotformAPIClient('YOUR API KEY')

    submissions = jotformAPIClient.get_submissions(0, 50, None, None)

    for submission in submissions:
        result = jotformAPIClient.delete_submission(submission["id"])
        print(result)

if __name__ == "__main__":
    main()
``` 

First the _JotformAPIClient_ class is included from the _jotform-api-python/jotform.py_ file. This class provides access to JotForm's API. You have to create an API client instance with your API key. 
In case of an exception (wrong authentication etc.), you can catch it or let it fail with a fatal error.
