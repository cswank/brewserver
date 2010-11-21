import unittest, json
from pyramid import testing
from base import BaseViewTests

class TankViewTests(BaseViewTests):
    def setUp(self):
        super(TankViewTests, self).setUp()
        self.context = self.front_page['hlt']

    def test_tank_view(self):
        from brewserver.views.tank_views import TankView
        request = testing.DummyRequest()
        view = TankView(self.context, request)
        info = view()
        self.assertEqual(info, {})

    def test_state_view(self):
        from brewserver.views.tank_views import StateView
        request = testing.DummyRequest()
        view = StateView(self.context, request)
        info = view()
        self.assertEqual(json.loads(info.body), {u'fill_valve': False, u'target_fill_temperature': None, u'burner': False, u'level_indicator': 0, u'target_volume': None, u'stirrer': False, u'thermometer': 0, u'target_temperature': None})

    

