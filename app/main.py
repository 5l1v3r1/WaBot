# -*- coding: utf-8 -*-
import string

from app.bot import bot
from app.utils import helper
from app.yesno.yesno import YesNo
from app.anime.anime import Anime
from app.quote.quote import Quote
from app.passwords import CLEVER_API_KEY
from app.clever.clever import Cleverbot
from app.quedada import quedada

####################################################################################################################


def handle_message(instance, command, predicate, message_entity, who, conversation):

    who_name = helper.sender_name(message_entity)

    if command == "hola":
        answer = "Hola *" + who_name + "*"
        bot.send_message(instance, answer, conversation)

    elif command == "ayuda":
        answer = "*Lista de comandos* \n!hola \n!anime \n!anime season \n!quote \n!siono \n!ayuda"
        bot.send_message(instance, answer, conversation)

    elif command == "siono":
        yesno = YesNo(instance, conversation)
        yesno.send_yesno()

    elif command == "anime":
        if predicate:
            if predicate == 'season':
                anime = Anime(instance, conversation, param='season')
            else:
                anime = Anime(instance, conversation, param=predicate)
        else:
            anime = Anime(instance, conversation)

        anime.send_anime()

    elif command == "quote":
        quote = Quote(instance, conversation)
        quote.send_quote()
    elif command == "quedada":

        args = [x for x in predicate.split(' ')]
        if len(args) <= 0:
            bot.send_message(instance, "Establece un lugar", conversation)
            return
        if len(args) >= 1:
            if args[0] == "finalizar":
                quedada.finish_quedada(instance, who, conversation)
                return
            if len(args) == 1:
                lugar = args[0]
                basic_boll = quedada.Quedada(instance, conversation, who, lugar)
                basic_boll.send_quedada()
    else:
        return
        #answer = cleverbot_answer(command + " " + predicate)
        #bot.send_message(instance, answer, conversation)


def cleverbot_answer(message):
    cb = Cleverbot(CLEVER_API_KEY)
    answer = cb.ask(message)
    return answer
