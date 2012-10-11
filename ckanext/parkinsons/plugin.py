import os
import json
from datetime import datetime
from genshi.input import HTML
from genshi.filters import Transformer
from pylons import request, tmpl_context as c
from ckan import model
from ckan.model.types import make_uuid
import ckan.lib.helpers as h
from ckan.lib.dictization.model_dictize import resource_dictize
from ckan.plugins import implements, SingletonPlugin, IRoutes, IConfigurer, \
    IConfigurable, IGenshiStreamFilter, IResourceUrlChange, IDomainObjectModification, IAuthFunctions, IActions
from ckan.logic import get_action
from ckan.logic import check_access

class ParkinsonsPlugin(SingletonPlugin):
    implements(IConfigurable)
    implements(IGenshiStreamFilter)
    implements(IRoutes, inherit=True)
    implements(IConfigurer, inherit=True)
    implements(IAuthFunctions)
    implements(IActions)
    
    def get_actions(self):
        """ 
        Should return a dict, the keys being the name of the logic 
        function and the values being the functions themselves.
        """         
        def parkinsons_test(context, data_dict):
            """\
            Test function from James
            """
            check_access('parkinsons_test', context, data_dict)
            model = context['model']
            user = context['user']
            result = data_dict.copy()
            result['user'] = user
            return result

        return {
            'parkinsons_test': parkinsons_test,
        }

    def get_auth_functions(self):
        """
        Returns a dict of all the authorization functions which the
        implementation overrides
        """
        def parkinsons_test(context, data_dict=None):
            model = context['model']
            user = context['user']
            if user:
                return {'success': True}
            else:
                return {'success': False, 'msg': 'Just testing.'}
            
        return {
            'parkinsons_test': parkinsons_test,
        }

    def configure(self, config):
        pass

    def update_config(self, config):
        here = os.path.dirname(__file__)

        template_dir = os.path.join(here, 'templates')
        public_dir = os.path.join(here, 'public')
        
        if config.get('extra_template_paths'):
            config['extra_template_paths'] += ','+template_dir
        else:
            config['extra_template_paths'] = template_dir
        if config.get('extra_public_paths'):
            config['extra_public_paths'] += ','+public_dir
        else:
            config['extra_public_paths'] = public_dir
        
    def after_map(self, map):
        return map

    def before_map(self, map):
        # Examples
        #controller = 'ckanext.parkinsons.controllers.parkinsons_login:ParkinsonsLoginController' 
        #map.connect('/user/logout', controller=controller, action='logout')
        return map

    def filter(self, stream):
         return stream
