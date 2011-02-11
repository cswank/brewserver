import json
from ..base_view import BaseView
from webob.exc import Response
from pyramid.url import model_url

class FrontPageView(BaseView):

    def __init__(self, context, request):
        super(FrontPageView, self).__init__(context, request)
        self.response = {
            'state_url': model_url(context, request, 'state.json'),
            'notification_url': model_url(context, request, 'notify'),
            }

class NotificationView(BaseView):

    def __init__(self, context, request):
        message = request.POST['post_message']
        notification_center = NotificationCenter()
        notification_center.post_message(message=message)
        self.response = Response(content_type="application/json", body=json.dumps({'result': 'ok'}))

class SetupView(BaseView):

    def __init__(self, context, request):
        super(SetupView, self).__init__(context, request)
        self.response = dict(
            save_setup_url=model_url(context, request, 'save-setup'),
            )

class SaveSetupView(BaseView):

    def __init__(self, context, request):
        super(SaveSetupView, self).__init__(context, request)
        setup = json.loads(request.body)
        print setup
        self.context.save_setup(setup)
        self.response = Response(content_type="application/json", body=json.dumps({'msg':'hi'}))
        

class StateView(BaseView):
    
    def __init__(self, context, request):
        state = context.state
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
        command = info['command']
        kw = info['kw']
        kw = dict([(str(key), value) for key, value in kw.iteritems()])
        context.set_state(command, kw)
        self.response = Response(content_type="application/json", body=json.dumps(dict(result='ok')))

