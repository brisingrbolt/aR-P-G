# In-game config menu will also be implemented here at some point.

def log(msg, msg_type = 'DEBUG'):
    if msg_type != 'DEBUG' or config.debug:
    print(msg_type + ": " + msg)

config = {
    debug = True
}
