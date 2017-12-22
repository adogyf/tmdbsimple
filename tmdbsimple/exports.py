# -*- coding: utf-8 -*-

"""
tmdbsimple.base
~~~~~~~~~~~~~~~
This module implements exports functions of tmdbsimple.

:license: GPLv3, see LICENSE for more details
"""

import datetime
import gzip
import requests


def get_exports(type_, date=datetime.date.today()):
    """
    Get a list of valid IDs and some higher level attributes that are
    helpful for filtering items like the adult, video and popularity values.
    See: https://developers.themoviedb.org/3/getting-started/daily-file-exports

    type_ choices:
        Movies: movie
        TV Series: tv_series
        People: person
        Collections: collection
        TV Networks  : tv_network
        Keywords: keyword
        Production Companies: production_company

    Args:
        type_: See lists above.
        date: datetime.date object.

    Returns:
        Daily File Exports as dict.
    """
    date = date.strftime('%m_%d_%Y')
    url = 'http://files.tmdb.org/p/exports/%s_ids_%s.json.gz' % (type_, date)
    r = requests.get(url)
    bytes_ = gzip.decompress(r.content)
    utf = bytes_.decode('utf-8')
    # data comes in format '{"foo":"bar"}\n{"foo":"bar"}\n'
    # and need to be edited in order to parse it as json
    edited = utf.replace('\n{', ',{')  # replace ever \n but the last
    j = json.loads('[%s]' % edited)
    return j
