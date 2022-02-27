from setuptools import setup

setup(
    name="asteroids",
    options = {
        'build_apps': {
            'include_patterns': [
                '**/*.png',
                '**/*.jpg',
                '**/*.egg',
            ],
            'gui_apps': {
                'asteroids': 'main.py',
            },
            'platforms': ['manylinux2010_x86_64'],
            'log_filename': '$USER_APPDATA/Asteroids/output.log',
            'log_append': False,
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ],
        }
    }
)
