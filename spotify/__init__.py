import tekore as tk

# Initialising Tekore
tk_config_file_location = input("Provide Tekore config file location: ")
config = tk.config_from_file(tk_config_file_location)
user_token = tk.prompt_for_user_token(*config, scope=tk.scope.every)  # Tighten scope eventually
spotify = tk.Spotify(user_token)

# Exclusion lists
exclusions = ['karaoke', 'the style of', 'tribute', 'originally performed by', 'includes hidden track',
              'bluegrass rendition', 'Live From The Royal Albert Hall', 'Ghostface UK Version', 'Spotify',
              'Djlilruben', 'djlilruben', 'Made Famous by', 'Bimbo Jones Radio Mix', 'Live Lounge']
blacklisted_artists = ['Karaoke', "Pickin' On Series", 'Midifine Systems', 'Studio Allstars',
                       'Grandes Canciones - Versiones Acústicas', 'Lucky Voice Karaoke', 'The Karaoke Channel',
                       'Ameritz', 'Poptastik Karaoke', "Singer's Edge Karaoke", 'Brazillian Bossa Nova',
                       'Nursery Rhymes 123', 'DJ Top Gun', 'Dj lil Ruben', 'Extreme DJs & Remixers']
