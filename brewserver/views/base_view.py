from pyramid.security import authenticated_userid
from pyramid.url import model_url

class BaseView(object):

    lineage_format = '<a href={url}>{name}</a>'

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        if isinstance(self.response, dict):
            self.response['lineage'] = self.lineage
        return self.response

    @property
    def lineage(self):
        output = ''
        return self._make_link(self.context, output)

    def _make_link(self, context, output):
        if context.__parent__ is None:
            return self.lineage_format.format(url=model_url(context, self.request), name='home') + output
        output = '<a> &rarr; </a>' + self.lineage_format.format(url=model_url(context, self.request), name=context.__name__) + output
        return self._make_link(context.__parent__, output)
