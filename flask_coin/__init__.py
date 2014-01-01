# -*- coding: utf-8 -*-
"""
    flask.ext.coin
    ~~~~~~~~~~~~~~

    Implements Bitcoin and Altcoin support for Flask applications.

    :copyright: (c) 2014 by Aaron Brady.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import
import os


from datetime import datetime
from flask import _request_ctx_stack
from urlparse import urlparse
from bitcoinrpc import connect_to_local, connect_to_remote
from werkzeug.local import LocalProxy


def _get_coin():
    from flask import current_app
    return current_app.coin_instance

def _coin_context_processor():
    return dict(current_coin=_get_coin())

current_coin = LocalProxy(lambda: _get_coin())

coin = LocalProxy(lambda: _get_coin().connection)

class Coin(object):
    """Central controller class that can be used to configure how
    Flask-Coin behaves.  Each application that wants to use Flask-Coin
    has to create, or run :meth:`init_app` on, an instance of this class
    after the configuration was initialized.
    """

    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Set up this instance for use with *app*, if no app was passed to
        the constructor.
        """
        self.app = app
        app.coin_instance = self
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['coin'] = self

        app.config.setdefault('COIN_RPC_URL', 'file:///tmp/bitcoin.conf')

        bits = urlparse(app.config['COIN_RPC_URL'])
        if bits.scheme == 'file':
            self.path = bits.path
            self.connection = connect_to_local(bits.path)
        else:
            hnp = None
            if '@' not in bits.netloc:
                raise ValueError("Refusing to connect to unauthenticated API endpoint")
            up, hnp = bits.netloc.rsplit('@', 1)
            self.username = up.split(':', 1)[0]
            self.password = up.split(':', 1)[-1]
            if ':' in hnp:
                self.hostname, port = hnp.split(':', 1)
                self.port = int(port)
            else:
                self.hostname = hnp
                self.port = 8332
            self.connection = connect_to_remote(self.username, self.password,
                                                host=self.hostname,
                                                port=self.port,
                                                use_https=bits.scheme == 'https')

        app.context_processor(_coin_context_processor)

