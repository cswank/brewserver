from pyramid.configuration import Configurator
from .models import get_root

def app(global_config, **settings):
    """ This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve``.
    """
    
    zcml_file = settings.get('configure_zcml', 'configure.zcml')
    config = Configurator(
        root_factory=get_root,
        settings=settings,
        )
    config.begin()
    config.load_zcml(zcml_file)
    config.end() 
    return config.make_wsgi_app()
