# youtube-playlist-creator
A project that creates a youtube from a list of songs' keywords

## How to use
(This project is still a work in progress so this version is just 
First you need to get a key that will allow you to use Youtube API. you need a google account then you can go and get your key here https://console.cloud.google.com/apis/credential

Second you need to substitute the value of DEVELOPER_KEY in search.py .

Once that's done you will need to install the needed packages and it's up to you if you want ti install it directly in your environment by running this command:
```shell
sudo pip install --upgrade google-api-python-client
```
or you are a good person that respects its environment and doesn't want to put everything on it, so you will create a virtualenv and install the package there. To do so you will run the following commands:
```shell
  virtualenv .venv
```
```shell
  source .venv/bin/activate
```
```shell
  pip install --upgrade google-api-python-client 
```
PS: 
 For the future when there will be many many packages, I will add a requirement.txt

Now you are all set to run the command that will return videos, channels, playlist that match keywords in keyword_list in youtube_playlist_creator.py.

Run the following command:
```shell
python youtube_playlist_creator.py
```
