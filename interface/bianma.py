
def utf8(obj):
    msg = str(obj)
    if not isinstance(msg, unicode):
        msg = msg.decode('unicode_escape', 'replace')
    return msg