Requirements:
Python (2.6 or higher)
A Google account with Google Drive enabled
Google API client and Google OAuth libraries

Installation:
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

Now, follow these steps to set up your Google account to work with Google Drive API.

Go to Google Cloud console(https://console.cloud.google.com/home) and sign in with your Google account.
Create a new project.
Go to APIs and Services.
Enable Google Drive API for this project.
Go to the OAuth Consent screen and configure the Consent screen for your project.
Enter the name of your application. It will be shown on the consent screen.
Now go to Credentials.
Click on Create credentials, and go to OAuth Client ID.
Enter your application’s name, and click Create.
Your Client ID will be created. Download it to your computer and save it as credentials.json

NOTE: Do not share your CLIENT ID or CLIENT SECRETS with anyone.
Now, we are done with the setup and installation

credentials.json file should have your data credentials and place in your project path.In this project I have made it empty now.
Unit test cases I have removed the personal data