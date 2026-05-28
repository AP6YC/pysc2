from pysc2.maps import lib

class MyCustomMap(lib.Map):
    directory = "Custom"  # The subfolder within the Maps directory
    filename = "Tigerclaw"   # The filename without the .SC2Map extension
    players = 2              # Number of players (usually 1 for mini-games)
    score_index = 0          # Index into score_cumulative for reward
