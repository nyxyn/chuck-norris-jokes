import hexchat
import threading
import requests
import html

CHANNEL_EVENT = 'Channel Message'
SELF_EVENT = 'Your Message'
KEYWORD = '.chuck'
CHANNEL_KEY = 'channel'
JOKES_URL = 'https://api.icndb.com/jokes/random'

__module_name__ = 'chuck_norris'
__module_version__ = '1.0'
__module_description__ = 'Say random Chuck Norris joke'


def get_joke():
    response = requests.get(JOKES_URL).json()
    value = response['value']
    return html.unescape(value['joke'])


def say(channel):
    joke = get_joke()
    command = 'msg {} <Chuck Norris Bot>: {}'.format(channel, joke)
    hexchat.command(command)


def print_callback(words, eol, userdata):
    message = words[1].lower()
    channel = hexchat.get_info(CHANNEL_KEY)

    if KEYWORD in message:
        thread = threading.Thread(target=say, args=(channel,))
        thread.start()

    return hexchat.EAT_NONE


hexchat.prnt('Setting hook for chuck norris...')
hexchat.hook_print(CHANNEL_EVENT, print_callback)
hexchat.hook_print(SELF_EVENT, print_callback)
hexchat.prnt('Hook set')

