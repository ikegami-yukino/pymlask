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

Cited by
=========

Scientific paper
-----------------
- Yingying Lao, Tomoya Kishida, Junqi Zhao, Dongli Han. A Practical and Emotional Response Technique: Context-Based Sticker Suggestion Model on the Line App. In Proceedings of the 8th International Conference on Frontiers of Educational Technologies (ICFET '22), p.162–168, 2022.
- 大澤　卓也. 「いじめ自殺」の社会問題に対するツイッター上の感情分析. 立命館産業社会論集, 第56巻, 第4号, p.85-104, 2021.
- Yoshihiro ADACHI, Tomohiro KONDO, Takamitsu KOBAYASHI, Nao ETANI, Kaito ISHII. Emotion Analysis of Japanese Sentences Using an Emotion-word Dictionary. Journal of the Visualization Society of Japan, Volume 41, Issue 161, p.21-27, 2022.
- 吉田　光男， 鳥海　不二夫， 榊　剛史. COVID-19流行下でのインフォデミック ―Twitterで流れたGoToトラベルに関する情報―. オペレーションズ・リサーチ, 2021年4月号, p.216-223, 2021.
- Tomoya Kitayama. COVID-19 and its impact on the national examination for pharmacists in Japan: An SNS text analysis. PLoS ONE, 18(6), 2023.
- 山田耕. コロナ禍の中で語られた「広島の観光」とは？ ― 広島観光客数を Twitter から予測する ―. 安田女子大学 現代ビジネス学会誌 2022 年度, Vol.11, p.28-56, 2023.
- 星野 雄介. ⾃然⾔語処理技術を⽤いた新型コロナウイルスに関する新聞社説の予備的分析 ―新聞社ごとの違いと研究の展望―. 武蔵野大学経営研究所紀要, 第5号, p.113-148, 2022.

Blog
------
- 【Python】PymlaskでML-ASK感情分析をやってみた話  |  ミナピピンの研究室: https://tkstock.site/2022/07/07/python-pymlask-ml-ask-emotion-naturallanguage/
- CentOS8にML-AskのPythonライブラリのインストール - 株式会社CoLabMix: https://colabmix.co.jp/tech-blog/centos8-ml-ask-python/
- VS Code上でPyML-Askを実行した際のImportError: https://teratail.com/questions/ex9rdi58hl634f

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
