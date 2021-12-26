from dadmatools.datasets import ARMAN
from dadmatools.datasets import get_all_datasets_info, get_dataset_info
from dadmatools.datasets import TEP
from dadmatools.datasets import PerSentLexicon
from dadmatools.datasets import FaSpell
from dadmatools.datasets import WikipediaCorpus
from dadmatools.datasets import PersianNer
from dadmatools.datasets import PersianNews
from dadmatools.datasets import PnSummary
from dadmatools.datasets import FarsTail
from dadmatools.datasets import SnappfoodSentiment
from dadmatools.datasets import get_all_datasets_info
from dadmatools.datasets import Peyma
from dadmatools.datasets import PerUDT
from dadmatools.datasets import PersianTweets


def test_overall():
    # print(get_all_datasets_info(tasks=['NER', 'Sentiment-Analysis']))
    print(get_dataset_info('Arman'))

def test_armna():
    arman = ARMAN()
    assert get_dataset_info('ARMAN')['task']  == 'NER'
    assert len(arman.test) == arman.info.size['test']

def test_fatail():
    fatail = FarsTail()
    assert get_dataset_info('FarsTail')['task'] == 'Textual-Entailment'
    assert len(fatail.test) == fatail.info.size['test']

def test_faspell():
    faspell = FaSpell()
    assert get_dataset_info('FaSpell')['task'] == 'Spell-Checking'
    assert len(faspell.ocr) == faspell.info.size['ocr']
    assert len(faspell.main) == faspell.info.size['main']

def test_persent():
    persent = PerSentLexicon()
    assert len(persent.data) == persent.info.size

def test_persian_news():
    pn = PersianNews()
    assert len(pn.test) == pn.info.size['test']
    assert len(pn.train) == pn.info.size['train']
    assert len(pn.dev) == pn.info.size['dev']

def test_perudt():
    perudt = PerUDT()
    assert len(perudt.test) == perudt.info.size['test']
    assert len(perudt.train) == perudt.info.size['train']
    assert len(perudt.dev) == perudt.info.size['dev']

def test_peyma():
    peyma = Peyma()
    assert len(peyma.data) == peyma.info.size


def test_pn_summary():
    arman = PnSummary()
    assert len(arman.test) == arman.info.size['test']


def test_snappfood_sentiment():
    sn = SnappfoodSentiment()
    assert len(sn.test) == sn.info.size['test']

def test_tep():
    arman = TEP()
    assert len(arman.test) == arman.info.size['test']

def test_tweets():
    tweets = PersianTweets()
    # assert len(arman.test) == arman.info.size['test']

# def test_tep():
#     tep = TEP()
#     assert len(tep.data) == tep.info.size

