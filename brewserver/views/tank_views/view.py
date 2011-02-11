import json
from webob.exc import Response
from ..base_view import BaseView
from pyramid.url import model_url
from pyrobot.brewery import BreweryError

class TankView(BaseView):

    def __init__(self, context, request):
        super(TankView, self).__init__(context, request)
        self.response = {
            'name': context.name,
            'devices': context.tank.devices.keys(),
            'state_url': model_url(context, request, 'state.json'),
            'history_url': model_url(context, request, 'history.json'),
            'calibration_curve_url': model_url(context, request, 'curve.json'),
            'send_command_url': model_url(context.__parent__, request, 'set-state'),
            'delete_point_url': model_url(context, request, 'delete-point'),
            'save_point_url': model_url(context, request, 'save-point'),
            'notification_url': model_url(context.__parent__, request, 'notify'),
            }

class StateView(BaseView):
    
    def __init__(self, context, request):
        state = context.__parent__.state
        self.response = Response(content_type="application/json", body=json.dumps(state))


class CalibrationCurveView(BaseView):
    
    def __init__(self, context, request):
        device = request.params['device']
        data = context.get_calibration_curve(device)
        self.response = Response(content_type="application/json", body=json.dumps(data))

class DeletePointView(BaseView):
    
    def __init__(self, context, request):
        point =  int(request.params['point'])
        device = request.params['device']
        try:
            context.delete_calibration_point(point, device)
        except BreweryError, e:
            body = {'error': str(e)}
        else:
            body = {'result':'ok'}
        self.response = Response(content_type="application/json", body=json.dumps(body))


class SavePointView(BaseView):
    
    def __init__(self, context, request):
        device = request.params['device']
        set_point =  float(request.params['set_point'])
        context.save_calibration_point(set_point, 'volume')
        self.response = Response(content_type="application/json", body=json.dumps({'result':'ok'}))

class HistoryView(BaseView):
    
    def __init__(self, context, request):
        self.response = Response(content_type="application/json", body=json.dumps(context.history))
