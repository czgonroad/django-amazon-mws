Views
=====
**MWSMixin**

Mix this in with your ``View`` class to provide ``marketplace`` and ``mws_credentials`` attributes on your view for the
logged in user. ``marketplace`` is by default the one with the code as set in your ``settings.py`` file
``DEFAULT_MARKETPLACE``, but can be changed by the user by specifying a different code in the query parameters e.g.
appending ``?marketplace=DE`` to the view's URL.