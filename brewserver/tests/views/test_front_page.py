import unittest
from pyramid import testing
from base import BaseViewTests

class FrontPageViewTests(BaseViewTests):
    def setUp(self):
        super(FrontPageViewTests, self).setUp()

    def test_front_page_view(self):
        from brewserver.views.front_page_views import FrontPageView
        request = testing.DummyRequest()
        view = FrontPageView(self.front_page, request)
        info = view()
        self.assertEqual(info, {})


