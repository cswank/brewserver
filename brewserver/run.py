from pyramid.configuration import Configurator
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.authentication import RepozeWho1AuthenticationPolicy
from .models import get_root

def app(global_config, **settings):
    """ This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve``.
    """
    
    zcml_file = settings.get('configure_zcml', 'configure.zcml')

    auth = RepozeWho1AuthenticationPolicy(identifier_name='basicauth')
    acl = ACLAuthorizationPolicy()

    config =  Configurator(
        root_factory=get_root,
        settings=settings,
        authorization_policy = acl,
        authentication_policy = auth,
        )
    config.begin()
    config.load_zcml(zcml_file)
    config.end() 
    return config.make_wsgi_app()
