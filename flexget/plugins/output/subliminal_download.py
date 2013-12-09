from __future__ import unicode_literals

import logging
from flexget.plugin import register_plugin, DependencyError
from babelfish.language import Language
import locale
import os
import subliminal

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
                    'opensubtitles' : {'type' : 'boolean', 'default' : True},
                    'thesubdb' : {'type' : 'boolean', 'default' : True},
                    'podnapisi' : {'type' : 'boolean', 'default' : True},
                    'addic7ed' : {'type' : 'boolean', 'default' : False},
                    'tvsubtitles' : {'type' : 'boolean', 'default' : True}
                },
                'additionalProperties' : False
            },
            'minimum_score' : { 'type' : 'number', 'default' : 0.0},
            'hearing_imparaired' : { 'type' : 'boolean', 'default' : False}
        },
        'additionalProperties' : False
    }
    
    def on_task_start(self, task, config):
        pass
        
    def on_task_output(self, task, config):
        languages = [
            Language(list(locale.getdefaultlocale())[1][0:2])
        ]
        for entry in task.accepted:
            if not entry['location']:
                entry.reject('no location for entry')
            elif not os.path.exists(entry['location']):
                entry.reject('file not found')
            else:
                videos = subliminal.scan_video(entry['location'])
                
                if videos is None:
                    entry.reject('No videos found in entry')
                else:
                    if not "languages" in config:
                        config = languages
                    subtitles = subliminal.download_best_subtitles(videos,
                                                                   config['languages'],
                                                                   config['accepted_providers'],
                                                                   provider_configs=None,
                                                                   min_score=config['minimum_score'],
                                                                   hearing_impaired=config['hearing_impaired'])
                    subliminal.save_subtitles(subtitles)
                
    
register_plugin(SubliminalDownload, "subliminal_download", api_ver=2)
