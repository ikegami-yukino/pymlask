# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
import os
import codecs
import re
import collections
import pkgutil
from sys import version_info
import MeCab


"""
ML-Ask (eMotive eLement and Expression Analysis system) is a keyword-based language-dependent system
for automatic affect annotation on utterances in Japanese.
It uses a two-step procedure:
1. Specifying whether a sentence is emotive, and
2. Recognizing particular emotion types in utterances described as emotive.

Original Perl version by Michal Ptaszynski
Python version by Yukino Ikegami
"""
PY2 = True if version_info < (3,) else False

# cvs stands for "Contextual Valence Shifters"
RE_PARTICLES = '[だとはでがはもならじゃちってんすあ]*'
RE_CVS = 'いまひとつもない|なくても?問題ない|わけに[はも]?いかない|わけに[はも]?いくまい|いまひとつない|ちょ?っとも?ない|なくても?大丈夫|今ひとつもない|訳にはいくまい|訳に[はも]?[行い]かない|そんなにない|ぜったいない|まったくない|すこしもない|いまいちない|ぜんぜんない|そもそもない|いけない|ゼッタイない|今ひとつない|今一つもない|行けない|あまりない|なくていい|なくても?OK|なくても?結構|少しもない|今一つない|今いちない|言えるない|いえるない|行かん|あかん|いかん|なくても?良い|てはだめ|[ちじ]ゃだめ|余りない|絶対ない|全くない|今一ない|全然ない|もんか|ものか|あるますん|ない|いない|思うない|思えるない|訳[がではもじゃ]*ない|わけ[がではもじゃ]?ない'
CVS_TABLE = {
    'suki': ['iya'],
    'ikari': ['yasu'],
    'kowa': ['yasu'],
    'yasu': ['ikari', 'takaburi', 'odoroki', 'haji', 'kowa'],
    'iya': ['yorokobi', 'suki'],
    'aware': ['suki', 'yorokobi', 'takaburi', 'odoroki', 'haji'],
    'takaburi': ['yasu', 'aware'],
    'odoroki': ['yasu', 'aware'],
    'haji': ['yasu', 'aware'],
    'yorokobi': ['iya']
}

# Compiling regular expression patterns
BRACKET = '\[|\(|\（|\【|\{|\〈|\［|\｛|\＜|\｜|\|'
EMOTICON_CHARS = '￣|◕|´|_|ﾟ|・|｀|\-|\^|\ |･|＾|ω|\`|＿|゜|∀|\/|Д|　|\~|д|T|▽|o|ー|\<|。|°|∇|；|ﾉ|\>|ε|\)|\(|≦|\;|\'|▼|⌒|\*|ノ|─|≧|ゝ|●|□|＜|＼|0|\.|○|━|＞|\||O|ｰ|\+|◎|｡|◇|艸|Ｔ|’|з|v|∩|x|┬|☆|＠|\,|\=|ヘ|ｪ|ェ|ｏ|△|／|ё|ロ|へ|０|\"|皿|．|3|つ|Å|、|σ|～|＝|U|\@|Θ|‘|u|c|┳|〃|ﾛ|ｴ|q|Ｏ|３|∪|ヽ|┏|エ|′|＋|〇|ρ|Ｕ|‐|A|┓|っ|ｖ|∧|曲|Ω|∂|■|､|\:|ˇ|p|i|ο|⊃|〓|Q|人|口|ι|Ａ|×|）|―|m|V|＊|ﾍ|\?|э|ｑ|（|，|P|┰|π|δ|ｗ|ｐ|★|I|┯|ｃ|≡|⊂|∋|L|炎|З|ｕ|ｍ|ｉ|⊥|◆|゛|w|益|一|│|о|ж|б|μ|Φ|Δ|→|ゞ|j|\\|\    |θ|ｘ|∈|∞|”|‥|¨|ﾞ|y|e|\]|8|凵|О|λ|メ|し|Ｌ|†|∵|←|〒|▲|\[|Y|\!|┛|с|υ|ν|Σ|Α|う|Ｉ|Ｃ|◯|∠|∨|↑|￥|♀|」|“|〆|ﾊ|n|l|d|b|X|ó|Ő|Å|癶|乂|工|ш|ч|х|н|Ч|Ц|Л|ψ|Ψ|Ο|Λ|Ι|ヮ|ム|ハ|テ|コ|す|ｙ|ｎ|ｌ|ｊ|Ｖ|Ｑ|√|≪|⊇|⊆|＄|″|♂|±|｜|ヾ|？|：|ﾝ|ｮ|f|\%|ò|å|冫|冖|丱|个|凸|┗|┼|ц|п|Ш|А|φ|τ|η|ζ|β|α|Γ|ン|ワ|ゥ|ぁ|ｚ|ｒ|ｋ|ｄ|ｂ|Ｘ|Ｐ|Ｈ|Ｄ|８|♪|≫|↓|＆|「|［|々|仝|!|ﾒ|ｼ|｣'
RE_EMOTICON = re.compile('('+BRACKET+')(['+EMOTICON_CHARS+']{3,}).*')
RE_POS = re.compile('感動|フィラー')
RE_MIDAS = re.compile('^(?:て|ね)(?:え|ぇ)$')
RE_KII = re.compile('^aware$|^haji$|^ikari$|^iya$|^kowa$|^odoroki$|^suki$|^takaburi$|^yasu$|^yorokobi$')
RE_VALANCE_POS = re.compile('yasu|yorokobi|suki')
RE_VALANCE_NEG = re.compile('iya|aware|ikari|kowa')
RE_VALANCE_NEU = re.compile('takaburi|odoroki|haji')
RE_ACTIVATION_A = re.compile('takaburi|odoroki|haji|ikari|kowa')
RE_ACTIVATION_D = re.compile('yasu|aware')
RE_ACTIVATION_N = re.compile('iya|yorokobi|suki')


class MLAsk(object):

    def __init__(self, mecab_arg=''):
        """Initialize MLAsk.

        Parameters
        ----------
        mecab_arg : str
            Argument parameters for MeCab.

        Examples
        --------
        >>> import mlask
        >>> mlask.MLAsk('-d /usr/local/lib/mecab/dic/ipadic')  #doctest: +ELLIPSIS
        <mlask.MLAsk object at 0x...>
        """
        if PY2:
            mecab_arg = mecab_arg.encode('utf8')
        self.mecab = MeCab.Tagger(mecab_arg)
        self._read_emodic()
        if not PY2:
            self.mecab.parse('')

    def _read_emodic(self):
        """ Load emotion dictionaries """

        self.emodic = {'emotem': {}, 'emotion': {}}

        # Reading dictionaries of syntactical indicator of emotiveness
        emotemy = ('interjections', 'exclamation', 'vulgar', 'endearments', 'emotikony', 'gitaigo')
        for emotem_class in emotemy:
            data = pkgutil.get_data('mlask',
                                    os.path.join('emotemes', '%s_uncoded.txt') % emotem_class)
            phrases = data.decode('utf8').splitlines()
            self.emodic['emotem'][emotem_class] = phrases

        # Reading dictionaries of emotion
        emotions = ('aware', 'haji', 'ikari', 'iya', 'kowa', 'odoroki', 'suki', 'takaburi', 'yasu', 'yorokobi')
        for emotion_class in emotions:
            data = pkgutil.get_data('mlask',
                                    os.path.join('emotions', '%s_uncoded.txt') % emotion_class)
            phrases = data.decode('utf8').splitlines()
            self.emodic['emotion'][emotion_class] = phrases

    def analyze(self, text):
        """ Detect emotion from text

        Parameters
        ----------
        text : str
            Target text.

        Return
        ------
        dict
            Result of emotion analysis.

        Examples
        --------
        >>> import mlask
        >>> ma = mlask.MLAsk()
        >>> ma.analyze('彼女のことが嫌いではない！(;´Д`)')
        {'text': '彼女のことが嫌いではない！(;´Д`)', 'emotion': defaultdict(<class 'list'>, {'iya': ['嫌'], 'yorokobi': ['嫌い*CVS'], 'suki': ['嫌い*CVS']}), 'orientation': 'mostly_POSITIVE', 'activation': 'ACTIVE', 'emoticon': ['(;´Д`)'], 'intension': 2, 'intensifier': {'exclamation': ['！'], 'emotikony': ['´Д`', 'Д`', '´Д', '(;´Д`)']}, 'representative': ('yorokobi', ['嫌い*CVS'])}
        """
        # Normalizing
        text = self._normalize(text)

        # Lemmatization by MeCab
        lemmas = self._lexical_analysis(text)

        # Finding emoticon
        emoticon = self._find_emoticon(text)

        # Finding intensifiers of emotiveness
        intensifier = self._find_emotem(lemmas, emoticon)
        intension = len(list(intensifier.values()))

        # Finding emotional words
        emotions = self._find_emotion(lemmas['all'])

        # Estimating sentiment orientation {POSITIVE, NEUTRAL, NEGATIVE}
        orientation = self._estimate_sentiment_orientation(emotions)

        # Estimating activeness {ACTIVE, NEUTRAL, PASSIVE}
        activation = self._estimate_activation(emotions)

        if emotions:
            result = {
                'text': text,
                'emotion': emotions,
                'orientation': orientation,
                'activation': activation,
                'emoticon': emoticon if emoticon else None,
                'intension': intension,
                'intensifier': intensifier,
                'representative': self._get_representative_emotion(emotions)
                }
        else:
            result = {
                'text': text,
                'emotion': None
                }
        return result

    def _normalize(self, text):
        text = text.replace('!', '！').replace('?', '？')
        return text

    def _lexical_analysis(self, text):
        """ By MeCab, doing lemmatisation and finding emotive indicator """
        lemmas = {'all': [], 'interjections': [], 'no_emotem': []}

        if PY2:
            text = text.encode('utf8')
        node = self.mecab.parseToNode(text)
        while node:
            try:
                if PY2:
                    surface = node.surface.decode('utf8')
                    features = node.feature.decode('utf8').split(',')
                else:
                    surface = node.surface
                    features = node.feature.split(',')
                if len(features) > 7:
                    (pos, subpos, lemma) = features[0], features[1], features[6]
                elif len(features) == 1:
                    pos = None
                    subpos = None
                    lemma = None
                else:
                    (pos, subpos, lemma) = features[0], features[1], surface
                if not pos is None and not subpos is None and not lemma is None:
                    lemmas['all'].append(lemma)
                    if RE_POS.search(pos + subpos) or RE_MIDAS.search(surface):
                        lemmas['interjections'].append(surface)
                    else:
                        lemmas['no_emotem'].append(surface)
            except UnicodeDecodeError:
                pass
            node = node.next

        lemmas['all'] = ''.join(lemmas['all']).replace('*', '')
        lemmas['no_emotem'] = ''.join(lemmas['no_emotem'])
        return lemmas

    def _find_emoticon(self, text):
        """ Finding emoticon """
        emoticons = []
        if RE_EMOTICON.search(text):
            emoticon = RE_EMOTICON.search(text).group(1) + RE_EMOTICON.search(text).group(2)
            emoticons.append(emoticon)
        return emoticons

    def _find_emotem(self, lemmas, emoticons):
        """ Finding syntactical indicator of emotiveness """
        emotemy = {}
        for (emotem_class, emotem_items) in self.emodic['emotem'].items():
            found = []
            for emotem_item in emotem_items:
                if emotem_item in lemmas['no_emotem']:
                    found.append(emotem_item)
            if emotem_class == 'emotikony':
                if len(emoticons) > 0:
                    found.append(','.join(emoticons))
            elif emotem_class == 'interjections':
                if len(lemmas['interjections']) > 0:
                    found.append(''.join(lemmas['interjections']))

            if len(found) > 0:
                found = [x for x in found if len(x) > 0]
                emotemy[emotem_class] = found
        return emotemy

    def _find_emotion(self, text):
        """ Finding emotion word by dictionaries """
        found_emotions = collections.defaultdict(list)
        for emotion_class, emotions in self.emodic['emotion'].items():
            for emotion in emotions:
                if emotion not in text:
                    continue
                cvs_regex = re.compile('%s(?:%s(%s))' % (emotion, RE_PARTICLES, RE_CVS))
                # if there is Contextual Valence Shifters
                if cvs_regex.findall(text):
                    for new_emotion_class in CVS_TABLE[emotion_class]:
                        found_emotions[new_emotion_class].append(emotion + "*CVS")
                else:
                    found_emotions[emotion_class].append(emotion)
        return found_emotions if found_emotions else None

    def _estimate_sentiment_orientation(self, emotions):
        """ Estimating sentiment orientation (POSITIVE, NEUTRAL, NEGATIVE) """
        orientation = ''
        if emotions:
            how_many_valence = ''.join(emotions.keys())
            how_many_valence = RE_VALANCE_POS.sub('P', how_many_valence)
            how_many_valence = RE_VALANCE_NEG.sub('N', how_many_valence)
            how_many_valence = RE_VALANCE_NEU.sub('NorP', how_many_valence)
            num_positive = how_many_valence.count('P')
            num_negative = how_many_valence.count('N')
            if num_negative == num_positive:
                orientation = 'NEUTRAL'
            else:
                if num_negative > 0 and num_positive > 0:
                    orientation += 'mostly_'
                orientation +='POSITIVE' if num_positive > num_negative else 'NEGATIVE'
            return orientation

    def _estimate_activation(self, emotions):
        """ Estimating activeness (ACTIVE, NEUTRAL, PASSIVE) """
        activation = ''
        if emotions:
            how_many_activation = ''.join(emotions.keys())
            how_many_activation = RE_ACTIVATION_A.sub('A', how_many_activation)
            how_many_activation = RE_ACTIVATION_D.sub('P', how_many_activation)
            how_many_activation = RE_ACTIVATION_N.sub('NEUTRAL', how_many_activation)
            count_activation_A = how_many_activation.count('A')
            count_activation_P = how_many_activation.count('P')

            if count_activation_A == count_activation_P:
                activation = 'NEUTRAL'
            else:
                if count_activation_A > 0 and count_activation_P > 0:
                    activation = 'mostly_'
                activation += 'ACTIVE' if count_activation_A > count_activation_P else 'PASSIVE'
            return activation

    def _get_representative_emotion(self, emotions):
        '''
        Extract emotion has most longest word from emotional words
        '''
        return sorted(emotions.items(), key=lambda x: len(x[1][0]), reverse=True)[0]
