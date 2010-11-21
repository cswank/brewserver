import json
from ..base_view import BaseView
from webob.exc import Response
from pyramid.url import model_url

class FrontPageView(BaseView):

    def __init__(self, context, request):
        super(FrontPageView, self).__init__(context, request)
        self.response = {
            'state_url': model_url(context, request, 'state.json'),
            }

class StateView(BaseView):
    
    def __init__(self, context, request):
        state = context.state
        print state
        self.response = Response(content_type="application/json", body=state)

class SetStatesView(BaseView):
    def __init__(self, context, request):
        infos = json.loads(request.body)
        for info in infos:
            command = info['command']
            kw = info['kw']
            kw = dict([(str(key), value) for key, value in kw.iteritems()])
            context.set_state(command, kw)
        self.response = Response(content_type="application/json", body=json.dumps(dict(result='ok')))


class SetStateView(BaseView):
    def __init__(self, context, request):
        info = json.loads(request.body)
        print info
        command = info['command']
        kw = info['kw']
        kw = dict([(str(key), value) for key, value in kw.iteritems()])
        context.set_state(command, kw)
        self.response = Response(content_type="application/json", body=json.dumps(dict(result='ok')))

