# youtube-playlist-creator
A project that creates a youtube from a list of songs' keywords

## Prerequirements
Before running this projet you need to make sure that you have google api credentials and that you can use two of Google APIs which are ```youtube data api``` and ```youtube analytics api```. And here are the steps to do so.

### Create google API OAuth credentials
- Go to https://console.developers.google.com/apis/credentials
- If you are not connected it will ask you to connect with your google account
- Next you will create credentials that will be used later on, click the blue button to create credential and choose ID client OAuth 

![Create credentials](/img/create_OAuth_id.PNG?raw=true)

- Then choose other from the list of application types and give the application the name ```youtube-playlist-creator``` and click create then ok

![Choose application type and name](/img/application_type_name.PNG?raw=true)

### Activate APIs
- Go to https://console.developers.google.com/apis/dashboard
- Then click on enable APIS AND SERVICES

![enable api menu](/img/enableAPI.PNG?raw=true)

- Go down to the section API Youtube

![youtube api section](/img/youtubeAPI.PNG?raw=true)

- Click on link ```Youtube Data API```
- Click on activate 

![activate Youtube data API](/img/enable_youtube_data_api.PNG?raw=true)

- Go back and do the same for ```YouTube Analytics API```

![activate Youtube analytics API](/img/youtube_analytics_API.PNG?raw=true)

## How to use 
First you need to clone this repository
```shell
git clone https://github.com/7rouz/youtube-playlist-creator.git
```

Then you need to download ID clients OAuth 2.0 file from here https://console.developers.google.com/apis/credentials, rename it client_secrets.json and put it in the project folder youtube_playlist_creator. 

![Download credentials](/img/DL_credentials.PNG?raw=true)

Second you need to create config.cfg (there is already config.cfg.sample to give you an idea how your config file should look like).

Next, you need to create keyword.txt file which contains songs keywords. Each line contains a song keywords. There is a keyword.txt.sample file for further details.

Once that's done you will need to install the needed packages and it's up to you if you want to install them directly in your environment by running this command:
```shell
sudo pip install -r requirements.txt
```
or you are a good person that respects its environment and doesn't want to put everything on it, so you will create a virtualenv and install requirements there. To do so you will run the following commands:
```shell
  virtualenv .venv
```
```shell
  source .venv/bin/activate
```
```shell
  pip install -r requirements.txt 
```

Now you are all set to create your playlist by running the following command:
```shell
python youtube_playlist_creator.py --noauth_local_webserver
```
you should see an url that you well need to go to to get a key to authenticate the script.

That's it. 
Now you should see for each song added
````
"Song title" has been added to "playlist name"
````

Once it's done you can go to your youtube channel and find the playlist that you have created.
Enjoy !