__author__ = 'jayk'

import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('secbot', re.IGNORECASE)
def hello_reply(message):
    message.reply('hello human!')


@respond_to('what is (.*)')
def whatis(message, something):
    message.reply('Here is {}'.format(something))