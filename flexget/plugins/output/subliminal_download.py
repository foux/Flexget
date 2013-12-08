from __future__ import unicode_literals

import logging
from flexget.plugin import register_plugin

log = logging.getLogger("subliminal_download");

class SubliminalDownload(object):
    
    schema = {
        'type' : 'object',
        'properties' : {
            'languages' : {
                'type' : 'array',
                'items' : {
                    'type' : 'string'
                },
                'additionalProperties' : False
            },
            'providers' : {
                'type' : 'object',
                'properties' : {
                    'opensubtitles' : {'type' : 'boolean', 'default' : 'true'},
                    'thesubdb' : {'type' : 'boolean', 'default' : 'true'},
                    'podnapisi' : {'type' : 'boolean', 'default' : 'true'},
                    'addic7ed' : {'type' : 'boolean', 'default' : 'false'},
                    'tvsubtitles' : {'type' : 'boolean', 'default' : 'true'}
                },
                'additionalProperties' : False
            },
            'minimum_score' : { 'type' : 'number', 'default' : '0.0'},
            'hearing_imparaired' : { 'type' : 'boolean', 'default' : 'false'}
        },
        'additionalProperties' : False
    }
    
    def process_config(self, config):
    
register_plugin(SubliminalDownload, "subliminal_download",api_ver=2)