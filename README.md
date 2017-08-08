# youtube-playlist-creator
A project that creates a youtube from a list of songs' keywords

## How to use 
First you need to get a key that will allow you to use Youtube API. you need a google accounti.
Then you need to download ID clients OAuth 2.0 file from here https://console.developers.google.com/apis/credentials, rename it client_secrets.json and put it in the project folder youtube_playlist_creator. 


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
