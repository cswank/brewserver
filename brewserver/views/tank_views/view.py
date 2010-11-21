import json
from webob.exc import Response
from ..base_view import BaseView
from pyramid.url import model_url

class TankView(BaseView):

    def __init__(self, context, request):
        super(TankView, self).__init__(context, request)
        self.response = {
            'name': context.name,
            'devices': context.tank.devices.keys(),
            'state_url': model_url(context, request, 'state.json'),
            'send_command_url': model_url(context.__parent__, request, 'set-state'),
            }

class StateView(BaseView):
    
    def __init__(self, context, request):
        state = context.state
        self.response = Response(content_type="application/json", body=json.dumps(state))


