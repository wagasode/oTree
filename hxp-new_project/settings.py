from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [dict(name='my_survey', num_demo_participants=None, app_sequence=['yamada_test_survey']),
        dict(name='test_yamada_public_goods', num_demo_participants=None, app_sequence=['test_yamada_public_goods']),
        dict(name='test_yamada_trust_game', num_demo_participants=None, app_sequence=['test_yamada_trust_game']),
        dict(name='test_yamada_prisoners_dilemma_game', num_demo_participants=None, app_sequence=['test_yamada_prisoners_dilemma_game'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


