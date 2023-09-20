from telegram.ext import BaseHandler

from Bot.Response import responses
from Bot.StateCTRL import AnyState, IdState
from Bot.Triggers import triggers


class UpdateProtocolUnit:
    def __init__(self, trigger_type, trigger_target, response_type, response, allowed_at_state, set_state):
        self.trigger_type = trigger_type
        self.trigger_target = trigger_target
        self.response_type = response_type
        self.response = response
        self.allowed_at_state = allowed_at_state
        self.set_state = set_state


def create_update_protocol_unit(data):
    return UpdateProtocolUnit(
        data["trigger_type"],
        data["trigger_target"],
        data["response_type"],
        data["response"],
        data["allowed_at_state"],
        data["set_state"]
    )


def create_update_protocol_units(json_data):
    update_protocol_units = []

    if "update_protocols" in json_data:
        update_protocol_data = json_data["update_protocols"]
        for key, data in update_protocol_data.items():
            update_protocol_unit = create_update_protocol_unit(data)
            update_protocol_units.append(update_protocol_unit)

    return update_protocol_units


def compile_protocol(conf_data) -> (str, [BaseHandler]):
    compiled: [BaseHandler] = []
    error: str = "All done"
    units = create_update_protocol_units(conf_data)

    for u in units:
        state_ctrl = AnyState() if u.allowed_at_state == "Any" else IdState(u.allowed_at_state)
        trigger = triggers[u.trigger_type](u.trigger_target)
        response = responses[u.response_type](u.response)

        def get_state():
            return "id_0"

        def set_sta():
            pass

        def none():
            pass

        set_state = set_sta if u.set_state != "keep" else none()

        async def callback(update, context):
            if state_ctrl.check_state(get_state()) and trigger.check_condition(update):
                await response.do_response(update, context)
                set_state()

        compiled.append(trigger.build_handler(callback))

    return error, compiled
