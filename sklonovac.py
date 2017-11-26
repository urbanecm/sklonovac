#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import re

RE_WORDS = re.compile("<x>[^<]*<")

def sklonujSlovo(word, pady=[1, 2, 3, 4, 5, 6, 7]):
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

def sklonujSlova(words=[], pady=[1, 2, 3, 4, 5, 6, 7]):
	res = {}
	for word in words:
		res[word] = sklonujSlovo(word, pady)
	return res
