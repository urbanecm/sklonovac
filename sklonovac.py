#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import re

RE_WORDS = re.compile("<x>[^<]*<")

def sklonujSlovo(wordRaw, pady=[1, 2, 3, 4, 5, 6, 7], sourcepad=1):
	if sourcepad != 1:
		url = "http://prirucka.ujc.cas.cz/?slovo=" + wordRaw
		r = requests.get(url)
		html = r.content
		RE_PAD = re.compile(".*1. pád.*", flags=re.MULTILINE)
		konkretniPad = RE_PAD.search(html).group(0).strip()
		RE_WORDS_2 = re.compile("<td class='centrovane'>[^<]*<")
		word = RE_WORDS_2.findall(konkretniPad)[0].replace("<td class='centrovane'>", "").replace("<", "")
	else:
		word = wordRaw
	url = "http://prirucka.ujc.cas.cz/?slovo=" + word
	r = requests.get(url)
	html = r.content
	res = {}
	for pad in pady:
		RE_PAD = re.compile(".*" + str(pad) + ". pád.*", flags=re.MULTILINE)
		konkretniPad = RE_PAD.search(html).group(0).strip()
		rawData = RE_WORDS.findall(konkretniPad)
		res[pad] = (rawData[0].replace('<x>', '').replace('<', ''), rawData[1].replace('<x>', '').replace('<', ''))
	return res

def sklonujSlova(words=[], pady=[1, 2, 3, 4, 5, 6, 7], sourcepad=1):
	res = {}
	for word in words:
		res[word] = sklonujSlovo(word, pady, sourcepad=1)
	return res
