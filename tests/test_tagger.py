import os
import pytest

from nltk.parse.corenlp import CoreNLPParser


O = 'O'
PERSON = 'PERSON'
ORGANIZATION = 'ORGANIZATION'
STATE_OR_PROVINCE = 'STATE_OR_PROVINCE'
CITY = 'CITY'


@pytest.fixture(scope='session')
def ner_tagger(corenlp_host_url):
    return CoreNLPParser(url=corenlp_host_url, tagtype='ner')

@pytest.mark.parametrize('text,tags', [
    ('Rami Eid is studying at Stony Brook University in NY', [
        ('Rami', PERSON),
        ('Eid', PERSON),
        ('is', O),
        ('studying', O),
        ('at', O),
        ('Stony', ORGANIZATION),
        ('Brook', ORGANIZATION),
        ('University', ORGANIZATION),
        ('in', O),
        ('NY', STATE_OR_PROVINCE),
    ]),
    ('Eid', [
        ('Eid', O),
    ]),
    ('Rami', [
        ('Rami', PERSON),
    ]),
    ('Stony', [
        ('Stony', O),
    ]),
    ('Brook', [
        ('Brook', PERSON),
    ]),
    ('University', [
        ('University', O),
    ]),
    ('Stony Brook', [
        ('Stony', CITY),
        ('Brook', CITY),
    ]),
])
def test_different_context_infer_different_tag(text, tags, ner_tagger):
    assert ner_tagger.tag(text.split()) == tags


# vi:et:ts=4:sw=4:cc=80
