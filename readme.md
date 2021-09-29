# Radio Stream to Spotify

Given a online radio stream URL, this program periodically checks for any
song title being returned by the stream metadata (the "now playing"), looks
it up on Spotify, and then adds it to a playlist.

This code will only work with streams that actually report the current song
playing in the metadata, and it needs to be in a readable format. I have
done much of the testing with Absolute Radio streams (UK), which do report the
current song playing most of the time.

## Prerequisites

* At least Python 3.6
* Tekore: https://pypi.org/project/tekore/

## Setting Up
A number of files need to be present for the program to work:

* **A Tekore config file**: Tekore is being set up from a configuration file which you will have to specify the location of when prompted. The contents of said file are detailed here: https://tekore.readthedocs.io/en/stable/advanced_usage.html#application-configuration
* **streams.txt**: This file is expected to be in the working directory, and holds the data for each stream you wish to be polling. It *must* contain all of the following information on a single line, separated by '@@@':
  * **Name**: the name of the stream,
  * **Url**: the stream url to poll,
  * **Encoding**: the encoding being used for the stream metadata (try latin1 first, or iso-8859-1 for mp3, or utf-8 for ogg)
  * **Regex**: a regular expression to be used for searching for the title amongst the metadata (try StreamTitle='(.*)';S)
  * **Separator**: the character that separates the track title from the track artist/s (eg, -)
  * **Order**: if the artist comes before the track title in the stream data, let this be 0. If it's the opposite, let this be 1.
  * **Playlist ID**: the Spotify ID for the playlist you wish this stations songs to be added to. To obtain, right click a playlist in the client, go to share, then copy Spotify URI and remove "spotify:playlist:" from the start to be left with the ID.
  * **Include Remixes?**: let this be 1 if you want to include remix tracks in the search, else let this be 0.
