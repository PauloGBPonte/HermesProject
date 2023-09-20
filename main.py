import json

from Bot import UpdateProtocol, bot_starter

with open("conf.json") as conf_file:
    conf_data = json.load(conf_file)
    compiled_protocol = UpdateProtocol.compile_protocol(conf_data)
    bot_starter.start_bot(compiled_protocol[1])

