# -*- coding: utf-8 -*-
import weechat
import time

weechat.register("ccflx", "__th0m", "0.1", "Colactron", "Circonflex me up", "", "")

def ccflx_cb(data, buffer, args):
    nick = weechat.buffer_get_string(weechat.current_buffer(), 'localvar_nick')
    repl = { 'a': 'â', 'c': 'ĉ', 'e': 'ê', 'g': 'ĝ', 'h': 'ĥ', 'i': 'î', 'j': 'ĵ', 'o': 'ô', 's': 'ŝ', 'u': 'û', 'w': 'ŵ', 'y': 'ŷ', 'z': 'ẑ' }
    for key, value in repl.iteritems():
        args = args.replace(key, value)
    weechat.command("", args)
    return weechat.WEECHAT_RC_OK

hook = weechat.hook_command("ccflx", "Circonflex me up", "text", "", "", "ccflx_cb", "")
