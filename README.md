# youtube-playlist-creator
[![PyPI pyversions](https://img.shields.io/badge/python-2.7-green)](https://www.python.org/downloads/release/python-2712/) [![PyPI license](https://img.shields.io/badge/licence-GPL3-green)](LICENSE)

To create a youtube playlist from a text file containing a list of songs. 

## Prerequirements
- python 2.7
- make sure that you have google api OAuth2 credentials
- Google APIs ```youtube data api``` and ```youtube analytics api``` enabled. 
You find how to do that in the next sections.

### Create google API OAuth credentials
  1. Choose or create a project to use.
  2. Go to "APIs & Services" \
    ![APIs and Services](/img/apis_services.PNG?raw=true)
  3. Go to "OAuth consent screen" to consent that you authorize the app to make action on your behave.
    we will go through the steps one by one:\
    - **first step**: choose external as shown in the following image\
      ![External application](/img/oauth_external_app.PNG?raw=true)
    - **second step**: OAuth consent screen:\
        * App information section:
            app name: youtube playlist creator
            user support email: your email
        * Developer contact information:
            email addresses: your email address
        * ==> click on "Save and continue"\
    - **third step**: Scopes\
      Scopes can be left empty because scopes are set by the application.\
      ==> click on "continue"
    - **fourth step**: Test users\
      Again nothing to do here. so go on and click "continue"
    - **fifth and final step**: publish app\
      Now that consent is over, you need to publish your application by clicking "publish app"\
      ![Publish application](/img/publish.PNG?raw=true)
  4. Go to https://console.developers.google.com/apis/credentials. Click "+ CREATE CREDENTIALS":\
      - **first step:** Application type.\
        choose from the list "Web application". it's confusing to use web application as type for an application that's technically a script. but don't worry about it. the application is faking a web application using 'google_auth_oauthlib.flow'.
      - **Second step:** configuring client ID\
        name : what ever you want to call the OAuth client ID (here I used the default value)\
        Authorized JavaScript origins: nothing here\
        Authorized redirect URIs: http://localhost:8080/\
      - click "create"\
        ![Create OAuth creds](/img/OAuth_creation.PNG?raw=true)
  5. Download OAuth client ID json.\
    ![Download OAuth creds](/img/download_OAuth_client_id.PNG?raw=true)

### Activate APIs
  - Go to https://console.developers.google.com/apis/dashboard
  - Then click on enable APIS AND SERVICES\
  ![enable api menu](/img/enableAPI.PNG?raw=true)
  - Go down to the section API Youtube\
  ![youtube api section](/img/youtubeAPI.PNG?raw=true)
  - Click on link ```Youtube Data API```
  - Click on activate \
  ![activate Youtube data API](/img/enable_youtube_data_api.PNG?raw=true)
  - Go back and do the same for ```YouTube Analytics API```\
  ![activate Youtube analytics API](/img/youtube_analytics_API.PNG?raw=true)

## How to use 
  First you need to clone this repository
  ```shell
  git clone https://github.com/7rouz/youtube-playlist-creator.git
  ``` 
  Then you need to download ID clients OAuth 2.0 file from here https://console.developers.google.com/apis/credentials, rename it client_secrets.json and put it in the project folder youtube_playlist_creator. \
  ![Download credentials](/img/download_OAuth_client_id.PNG?raw=true)\
  Second you need to create config.cfg (there is already config.cfg.sample to give you an idea how your config file should look like).\
  Next, you need to create keyword.txt file which contains songs keywords. Each line contains a song keywords. There is a keyword.txt.sample file for further details.\
  Once that's done you will need to install the needed packages and it's up to you if you want to install them directly in your environment by running this command:
  ```shell
  sudo pip install -r requirements.txt
  ```
  or you are a good person that respects its environment and doesn't want to put everything on it, so you will create a virtualenv and install requirements there. To do so you will run the following commands:
  ```shell
    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt 
  ```
  Now you are all set to create your playlist by running the following command:
  ```shell
  python youtube_playlist_creator.py --noauth_local_webserver
  ```
  you should see an url that you well need to go to to get a key to authenticate the script.\
  That's it. \
  Now you should see for each song added
  ````
  "Song title" has been added to "playlist name"
  ````

  Once it's done you can go to your youtube channel and find the playlist that you have created.\
  Enjoy !