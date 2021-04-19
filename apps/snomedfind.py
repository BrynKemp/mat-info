from urllib.request import urlopen
from urllib.parse import quote
import json
import numpy as np
import urllib.request, urllib.error, urllib.parse
import json
import re
import os
from pprint import pprint
from stop_words import get_stop_words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from stop_words import get_stop_words
from gensim.parsing.preprocessing import remove_stopwords
import re
import math
import itertools
import contextlib

baseUrl = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct'
edition = 'MAIN'
version = '2019-07-31'

terms = []
snomed_codes = []
snomed_strings = []

def processstring(stringin):
    words = remove_stopwords(stringin)
    words = words.split()
    strings = []
    s = ' '.join(words)
    # s = words

    repin = ['3a tear', '3b tear', '3c tear', '3rd degree tear', '4th degree tear', 'caesarean', 'cs', 'cat 1',
             'category 1',
             'dm', 'dvt', 'erpc', 'fourth degree tear', 'gbs', 'haemorrhage', 'iud', 'kiellands', 'kiwi', 'krfd',
             'lscs', 'mec', 'moh',
             'mrop', 'nbfd', 'nead', 'oasi', 'pathological ctg', 'pe', 'pet', 'pih', 'pph', 'rpoc',
             'sah', 'sga', 'smm', 'srom', 'svt', 'third degree tear', 'tia', 'top', 'vbac']
    repout = ['repair of obstetric laceration of anal sphincter',
              'repair of obstetric laceration of anal sphincter',
              'repair of obstetric laceration of anal sphincter',
              'repair of obstetric laceration of anal sphincter',
              'repair of obstetric laceration of anal sphincter',
              'cesarean',
              'cesarean section',
              'fetal distress',
              'fetal distress',
              'diabetes',
              'deep vein thrombosis',
              'evacuation of retained product of conception',
              'repair of obstetric laceration of anal sphincter',
              'streptococcus agalactiae',
              'hemorrhage',
              'intrauterine death',
              'delivery by kiellands rotation',
              'ventouse',
              'delivery by kiellands rotation',
              'lower segment cesarean section',
              'meconium',
              'postpartum hemorrhage',
              'manual removal of placenta',
              'non epilepsy attack disorder',
              'instrumental delivery',
              'repair of obstetric laceration of anal sphincter',
              'fetal distress',
              'pulmonary embolus',
              'preeclampsia',
              'pregnancy induced hypertension',
              'postpartum hemorrhage',
              'evacuation of retained product of conception',
              'subarrachnoid hemorrhage',
              'small for gestational age',
              'evacuation of retained product of conception',
              'spontaneous rupture of membranes',
              'supraventricular tacycardia',
              'repair of obstetric laceration of anal sphincter',
              'transient ischemic attack',
              'termination of pregnancy',
              'vaginal birth after cesarean section']

    for a in range(len(repin)):
        t_in = repin[a]
        t_out = repout[a]
        swaptest = re.compile(r'\b{}\b'.format(t_in))
        res1 = re.findall(swaptest, s)
        if res1 != []:
            s = s.replace(t_in, t_out)
            res1 = []

    return s


# Prints fsn of a concept
def getConceptById(id):
    baseUrl = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct'
    edition = 'MAIN'
    version = '2019-07-31'
    url = baseUrl + '/browser/' + edition + '/' + version + '/concepts/' + id
    response = urlopen(url).read()
    data = json.loads(response.decode('utf-8'))
    print(data['fsn']['term'])


# Prints description by id
def getDescriptionById(id):
    baseUrl = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct'
    edition = 'MAIN'
    version = '2019-07-31'
    url = baseUrl + '/' + edition + '/' + version + '/descriptions/' + id
    response = urlopen(url).read()
    data = json.loads(response.decode('utf-8'))
    print(data['term'])


# Prints number of concepts with descriptions containing the search term
def getConceptsByString(searchTerm):
    baseUrl = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct'
    edition = 'MAIN'
    version = '2019-07-31'
    url = baseUrl + '/browser/' + edition + '/' + version + '/concepts?term=' + quote(
        searchTerm) + '&activeFilter=true&offset=0&limit=50'
    response = urlopen(url).read()
    data = json.loads(response.decode('utf-8'))
    return (data['total'])


# Prints number of descriptions containing the search term with a specific semantic tag
def getDescriptionsByStringFromProcedure(searchTerm, semanticTag):
    baseUrl = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct'
    edition = 'MAIN'
    version = '2019-07-31'
    url = baseUrl + '/browser/' + edition + '/' + version + '/descriptions?term=' + quote(
        searchTerm) + '&conceptActive=true&semanticTag=' + quote(
        semanticTag) + '&groupByConcept=false&searchMode=STANDARD&offset=0&limit=50'
    with contextlib.closing(urlopen(url)) as x:
        response = x.read()
        data = json.loads(response.decode('utf-8'))

    item_snomedstring = []
    item_snomedcode = []
    lookups = len(data['items'])

    for a in range(lookups):
        item_snomedcode.append(data['items'][a]['term'])
        item_snomedstring.append(data['items'][a]['concept']['id'])

    return item_snomedcode, item_snomedstring


# getConceptById('109152007')
# getConceptById('109152007')
# getDescriptionById('66214007')
# getConceptsByString('substance misuser')
# getConceptsByString(''neville barnes forcep')
# getDescriptionsByStringFromProcedure('drug abuse', '')

def getsnomed(words):
    outputstrings = np.zeros([100, 30], dtype='object')
    outputcodes = np.zeros([100, 30], dtype='object')
    outputid = range(0, 29, 2)
    tempstrings = []
    snomedcount = []
    snomedprcount = []

    for b in range(len(words)):
        exec(f'strlist_{b} = list(range(0,b+2))')
        exec(f'str_{b} = words[strlist_{b}[0]:strlist_{b}[-1]]')
        if b == 0:
            exec(f'sr_{b} = words[0]')
            exec(f'tempstrings.append(words[0])')

        if b > 0:
            exec(f'sr_{b} = sr_{b - 1} + " " + words[{b}]')
            exec(f'tempstrings.append(sr_{b - 1} + " " + words[{b}])')

    itemcount = len(tempstrings)

    for c in range(itemcount):
        tempstring = tempstrings[c]
        item_snomedcodepr, item_snomedstringpr = getDescriptionsByStringFromProcedure(tempstring,
                                                                                      "procedure")
        item_snomedcodenp, item_snomedstringnp = getDescriptionsByStringFromProcedure(tempstring, "")
        snomedcodes = np.concatenate((item_snomedstringpr, item_snomedstringnp))
        snomedstrings = np.concatenate((item_snomedcodepr, item_snomedcodenp))
        snomedcodes = np.unique(snomedcodes, axis=0)
        snomedstrings = np.unique(snomedstrings, axis=0)
        outputstrings[0, c] = tempstring
        outputcodes[0, c] = tempstring
        outputstrings[1, c] = len(snomedstrings)
        outputcodes[1, c] = len(snomedcodes)

        for d in range(len(snomedcodes)):
            outputstrings[2 + d, c] = snomedstrings[d]
            outputcodes[2 + d, c] = int(snomedcodes[d])

    return outputcodes, outputstrings


def retrievecoding(test_str):
    terms = []
    snomed_codes = []
    snomed_strings = []
    snomed = []
    words = processstring(test_str)
    meaning = 0
    words = words.split()
    origin_words = words

    while len(words[meaning:]) > 0:
        words = words[meaning:]
        outputcodes, outputstrings = getsnomed(words)
        meaning = outputcodes[1] == 0
        meaning = ([i for i, x in enumerate(meaning) if x])[0]
        terms.append(' '.join(words[:meaning]))
        tempcode = outputcodes[0:, meaning - 1] != 0
        tempcode = [i for i, x in enumerate(tempcode) if x]
        codeloci = len(tempcode) - 2
        snomed_codes.append(outputcodes[2:2 + codeloci, meaning - 1])

        for b in range(len(snomed_codes)):
            if isinstance(snomed_codes[b], int):
                snomed.append(snomed_codes[b])
            if isinstance(snomed_codes[b], (np.ndarray, list)):
                for c in range(len(snomed_codes[b])):
                    snomed.append((snomed_codes[b])[c])

    return terms, snomed



banana = retrievecoding('Eclamptic seizure')
