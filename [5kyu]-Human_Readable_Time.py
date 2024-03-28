def make_readable(time):
    hours = str(time // 3600)
    minutes = str(time // 60 % 60)
    seconds = str(time % 60)
    return ((2 - len(hours)) * "0") + hours + ":" + ((2 - len(minutes)) * "0") + minutes + ":" + ((2 - len(seconds)) * "0") + seconds
