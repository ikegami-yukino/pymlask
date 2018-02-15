pymlask
===================

|travis| |coveralls| |pyversion| |version|  |landscape|  |license|

pymlask is a Python version of ML-Ask (eMotive eLement and Expression Analysis system)

For details about ML-Ask, See http://arakilab.media.eng.hokudai.ac.jp/~ptaszynski/repository/mlask.htm

See also http://qiita.com/yukinoi/items/ef6fb48b5e3694e9659c (in Japanese)

Contributions are welcome!


Installation
==============
Modified dictionary version

::

 pip install pymlask

ML-Ask Original dictionary version

::

 pip install git+https://github.com/ikegami-yukino/pymlask@original

Example
===========

.. code:: python

 from mlask import MLAsk
 emotion_analyzer = MLAsk()
 emotion_analyzer.analyze('彼のことは嫌いではない！(;´Д`)')
 # => {'text': '彼のことは嫌いではない！(;´Д`)',
 #     'emotion': defaultdict(<class 'list'>,{'yorokobi': ['嫌い*CVS'], 'suki': ['嫌い*CVS'], 'iya': ['嫌']}),
 #     'orientation': 'mostly_POSITIVE',
 #     'activation': 'ACTIVE',
 #     'emoticon': ['(;´Д`)'],
 #     'intension': 2,
 #     'intensifier': {'exclamation': ['！'], 'emotikony': ['´Д`', 'Д`', '´Д', '(;´Д`)']},
 #     'representative': ('yorokobi', ['嫌い*CVS'])
 #     }


LICENSE
=========

The BSD 3-Clause License


Copyright
=============

ML-Ask Python: The BSD 3-Clause License
(c) 2017 Yukino Ikegami. All Rights Reserved.

ML-Ask (original): The BSD 3-Clause License
(c) 2007-2013, Michal Ptaszynski, Pawel Dybala, Rafal Rzepka, Kenji Arakii. All Rights Reserved.

.. |travis| image:: https://travis-ci.org/ikegami-yukino/pymlask.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/pymlask
    :alt: travis-ci.org

.. |coveralls| image:: https://coveralls.io/repos/ikegami-yukino/pymlask/badge.png
    :target: https://coveralls.io/r/ikegami-yukino/pymlask
    :alt: coveralls.io

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/pymlask.svg

.. |version| image:: https://img.shields.io/pypi/v/pymlask.svg
    :target: http://pypi.python.org/pypi/pymlask/
    :alt: latest version

.. |landscape| image:: https://landscape.io/github/ikegami-yukino/pymlask/master/landscape.svg?style=flat
   :target: https://landscape.io/github/ikegami-yukino/pymlask/master
   :alt: Code Health

.. |license| image:: https://img.shields.io/pypi/l/mlask.svg
    :target: http://pypi.python.org/pypi/mlask/
    :alt: license
