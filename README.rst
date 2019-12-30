pymlask
===================

|travis| |coveralls| |pyversion| |version| |license|

pymlask is a Python version of ML-Ask (eMotive eLement and Expression Analysis system)

For details about ML-Ask, See http://arakilab.media.eng.hokudai.ac.jp/~ptaszynski/repository/mlask.htm

See also http://qiita.com/yukinoi/items/ef6fb48b5e3694e9659c (in Japanese)

Contributions are welcome!

Dependencies
==============
MeCab binary
-------------

* Windows (32-bit Python): https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7WElGUGt6ejlpVXc
* Windows (64-bit Python): https://github.com/ikegami-yukino/mecab/releases
* macOS with Homebrew: $ brew install mecab mecab-ipadic
* Ubuntu: $ sudo apt install mecab libmecab-dev mecab-ipadic-utf8

Installation
==============
Modified dictionary version (recommended)

::

 pip install pymlask

ML-Ask Original dictionary version (same as Ptaszynski's Perl version)

::

 pip install git+https://github.com/ikegami-yukino/pymlask@original

Example
===========

.. code:: python

 from mlask import MLAsk
 emotion_analyzer = MLAsk()
 emotion_analyzer.analyze('彼のことは嫌いではない！(;´Д`)')
 # => {'text': '彼のことは嫌いではない！(;´Д`)',
 #     'emotion': defaultdict(<class 'list'>,{'yorokobi': ['嫌い*CVS'], 'suki': ['嫌い*CVS']}),
 #     'orientation': 'POSITIVE',
 #     'activation': 'NEUTRAL',
 #     'emoticon': ['(;´Д`)'],
 #     'intension': 2,
 #     'intensifier': {'exclamation': ['！'], 'emotikony': ['´Д`', 'Д`', '´Д', '(;´Д`)']},
 #     'representative': ('yorokobi', ['嫌い*CVS'])
 #     }
 emotion_analyzer = mlask.MLAsk('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')  # Use other dictionary

Dictionary sources
====================
* 中村 明 (1993) "感情表現辞典" 東京堂出版
* 学研辞典編集部 (2017) "感情ことば選び辞典" 学研プラス
* Angela Ackerman, Becca Puglisi (2012) "The Emotion Thesaurus: A Writer's Guide to Character Expression" JADD Publishing. (滝本 杏奈 (訳) (2015) "感情類語辞典" フィルムアート社)
* Angela Ackerman, Becca Puglisi (2013) "The Positive Trait Thesaurus: A Writer's Guide to Character Attributes" JADD Publishing (滝本 杏奈 (訳) (2016) "性格類語辞典 ポジティブ編" フィルムアート社)
* Angela Ackerman, Becca Puglisi (2013) "The Negative Trait Thesaurus: A Writer's Guide to Character Attributes" JADD Publishing (滝本 杏奈 (訳) (2016) "性格類語辞典 ポジティブ編" フィルムアート社)

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

.. |license| image:: https://img.shields.io/pypi/l/mlask.svg
    :target: http://pypi.python.org/pypi/mlask/
    :alt: license
