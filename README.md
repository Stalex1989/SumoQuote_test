# SumoQuote_test
- Python (3.11.3 version)/Poetry (version 1.5.1)/faker (18.11.2 version)
    1. Install python 
    2. Install pip 'py -m pip install'
    3. Install Poetry '(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -'
    4. Install Petest 'pip install -U pytest'
    5. Install Faker 'pip install Faker'
- There are 2 test files, the first - sign-up page and the second - adding profile information. I've left some comments in those files.
- Description the first file (test_sign_up.py): 
      1. In this test I implemented random generation for all form fields.
      2. I've been trying to implement API request to the Tempmail, and use it in the test, but I need to learn a little bit more how to use this.
      3. Also tryed to create a separete file for data generation, but had an issue with using functions form separeted file.
- Description the second file (test_completing_profile.py):
      1. In this test I used a email that is already pased the verification.
      2. Faced with some issues, all of them described in the comments.
- Before starting the execution of this test task, I planned to add more checks and implement some additional things (for example, getting a mail address using the request API), but I still lack experience with this framework.
- Please note that this is my first experience with Python and Pytest. Thanks in advance.   
