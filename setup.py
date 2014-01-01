"""
Flask-Coin
----------

Adds Bitcoin and Altcoin support to Flask applications with the help of the
`bitcoin-python`_ library.

"""
from setuptools import setup


setup(
    name='Flask-Coin',
    version='0.1',
    url='http://github.com/insom/flask-coin',
    license='BSD',
    author='Aaron Brady',
    author_email='aaron@insom.me.uk',
    description='Adds Bitcoin and Altcoin support to Flask applications',
    long_description=__doc__,
    packages=['flask_coin'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'bitcoin-python>=0.3',
        'Jinja2'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
