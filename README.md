# Liked VS. Lineup
A script that compares music festival lineups with the bands that are in your Spotify liked songs playlist.

Uses [Spotipy](https://github.com/plamere/spotipy)

# Get yourself running

## Install packages
```
$ conda create --name liked_lineup --file requirements.txt
Windows:
$ conda activate liked_lineup
Linux/Mac OS:
$ conda source activate liked_lineup

OR in an existing environment:
$ pip install -r requirements.txt
```

## Create your Spotify credentials and App
1. [Create a developer account](https://developer.spotify.com/)
2. [Create an app and call it whatever you want](https://developer.spotify.com/dashboard/applications)
3. Copy your `client ID` and `client secret` to an environment file `spotify.env`.
4. Add the spotify accounts you are searching to this app
5. Set the app's redirect URI to something like `http://localhost` or your website

![image](https://user-images.githubusercontent.com/30810522/160060609-d69ef7a6-c2c8-4ac7-9781-ffb141dbec33.png)

## Create spotify.env
```
# From App page:
YOUR_APP_CLIENT_ID=`abcdef
# Given to you when you create your app:
YOUR_APP_CLIENT_SECRET=`12345` 
YOUR_APP_REDIRECT_URI=http://localhost 
# ... or whatever you want to set this to (has to match 100% with what you set on your app)
```
## Lineup CSV
Currently this repo contains the bands performing at EDC Las Vegas 2022. I've also included those who performed at SXSW 2022.

These CSVs are formatted as 1 column with the word 'Band' in the header and the artists below this header.

You can change what CSV is loaded by changing this on line 11:
```
# CSV of lineup
lineup = pd.read_csv("your_cool_festival_2025.csv")
```

## Running
When you run this script for the first time you'll get a browser window to authenticate with Spotify then will likely take you to a broken webpage. Copy this URL into the console where it says:
```
Enter the URL you were redirected to: 
```
This will create a `.cache` file in your working directory which will contain the credentials to access your account. To change accounts, delete this file.

## Results
The console will return the artists found that match those in your spotify liked songs!

```
Found Artist: BLUE MAYZE
Found Artist: MADEON 
Found Artist: WILLIE NELSON
```
