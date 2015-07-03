import weechat
import time

weechat.register("bowbaq", "__th0m", "0.1", "Colactron", "Bowbaq facts", "", "")

def bowbaq_cb(data, buffer, args):
    nick = weechat.buffer_get_string(weechat.current_buffer(), 'localvar_nick')
    weechat.command("", "/nick bowbaq_")
    weechat.command("", args)
    weechat.command("", "/nick %s" % nick)
    return weechat.WEECHAT_RC_OK

hook = weechat.hook_command("bowbaq", "Bowbaq facts", "text", "", "", "bowbaq_cb", "")
