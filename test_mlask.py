# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nose.tools import assert_equals, assert_true, assert_false, assert_raises
from mlask import MLAsk

mla = MLAsk()

def test__read_emodic():
    assert_true('！' in mla.emodic['emotem']['exclamation'])
    assert_true('嫌い' in mla.emodic['emotion']['iya'])

def test_analyze():
    result = mla.analyze('彼は嫌いではない！(;´Д`)')
    assert_equals(result['text'], '彼は嫌いではない！(;´Д`)')

def test__normalize():
    assert_equals(mla._normalize('!'), '！')
    assert_equals(mla._normalize('?'), '？')

def test__lexical_analysis():
    assert_equals(mla._lexical_analysis('すごい'),
                  {'all': 'すごい', 'interjections': [], 'no_emotem': 'すごい'})

def test__find_emoticon():
    assert_equals(mla._find_emoticon('(;´Д`)'), ['(;´Д`)'])
    assert_equals(mla._find_emoticon('顔文字なし'), [])

def test__find_emotem():
    assert_equals(mla._find_emotem({'no_emotem': '(;´Д`)', 'interjections': '！'}, []),
                  {'emotikony': ['´Д`', 'Д`', '´Д'], 'interjections': ['！']})

def test__find_emotion():
    assert_equals(mla._find_emotion('嫌い'), {'iya': ['嫌', '嫌い']})

def test__estimate_sentiment_orientation():
    assert_equals(mla._estimate_sentiment_orientation({'iya': ['嫌い', '嫌']}), 'NEGATIVE')

def test__estimate_activation():
    assert_equals(mla._estimate_activation({'iya': ['嫌い', '嫌']}), 'ACTIVE')

def test__get_representative_emotion():
    assert_equals(mla._get_representative_emotion({'iya': ['嫌い', '嫌']}), ('iya', ['嫌い', '嫌']))
