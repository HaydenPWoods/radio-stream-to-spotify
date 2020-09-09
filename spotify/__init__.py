import tekore as tk

# Initialising Tekore
tk_config_file_location = input("Provide Tekore config file location: ")
config = tk.config_from_file(tk_config_file_location)
user_token = tk.prompt_for_user_token(*config, scope=tk.scope.every)  # Tighten scope eventually
spotify = tk.Spotify(user_token)
