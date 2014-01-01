Flask-Coin
===========

.. module:: flask.ext.coin

Flask-Coin is an extension to `Flask`_ that adds Bitcoin and Altcoin support to
any Flask application with the help of `bitcoin-python`_.

Installation
------------

Install the extension with one of the following commands::

    $ easy_install Flask-Coin

or alternatively if you have pip installed::

    $ pip install Flask-Coin


Configuration
-------------

To get started all you need to do is to instanciate a :class:`Coin`
object after configuring the application::

    from flask import Flask
    from flask.ext.coin import Coin, coin

    app = Flask(__name__)
    app.config.from_pyfile('mysettings.cfg')
    c = Coin(app)

    @app.route('/')
    def main():
        return coin.getaccountaddress('')

The `coin` variable imported from :mod:`flask.ext.coin` always uses
the connection bound to the current Flask application context.

Coin has one configuration value that can be used to change some internal
defaults:

=========================== =============================================
`COIN_RPC_URL`              The default URL to use for communicating with
                            bitcoind. This can be an `https`, `http` or
                            `file` URL and defaults to
                            ``'file:///tmp/bitcoin.conf'``.
=========================== =============================================

API
---

This part of the documentation documents each and every public class or
function from Flask-Coin.

Configuration
`````````````

.. autoclass:: Coin
   :members:

Credits
-------

Coin logo used above from "`A Dictionary of Roman Coins`_", Stevenson, Smith and Madden, 1889.

.. _Flask: http://flask.pocoo.org/
.. _bitcoin-python: https://pypi.python.org/pypi/bitcoin-python
.. _A Dictionary of Roman Coins: http://www.forumancientcoins.com/numiswiki/view.asp?key=dictionary%20of%20roman%20coins
