from setuptools import setup

setup(
    name='xblock-codeeditor',
    version='0.1',
    description='codeeditor XBlock ',
    py_modules=['codeeditor'],
    install_requires=['XBlock'],
    entry_points={
        'xblock.v1': [
            'codeeditor = codeeditor:CodeeditorBlock',
        ]
    }
)