#####################################################################
# Spark Listener
#
# Run in a separate thread, posts to a callback url on value change
#
# Code originally written by paulhamsh.
# See https://github.com/paulhamsh/Spark-Parser
#####################################################################

import requests

def listen(reader, comms, url):            
    while True:
        try:
            dat = comms.get_data()            
            reader.set_message(dat)
            reader.read_message()                       
            
            if reader.python is None:
                continue

            requests.post(url, json = reader.python)
        except:
            requests.post(url, json = '{"ConnectionLost": True}')
            break
        