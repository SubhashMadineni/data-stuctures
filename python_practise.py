# -*- coding: utf-8 -*-
"""python practise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I6tnfG-lH1Rcs50ueUoH-6QTNVODjK2R
"""

import tensorflow as tf

import random

letters = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

end = (''.join(random.choice(letters) for i in range(10)))
print(end)

u = ("http://tinyurl.com/4e9iAk").split('com/')[1]
print(u)

import random
class Codec:
    urldict = {}
    def encode(self, longUrl: str) -> str:
        urldict = {}
        """Encodes a URL to a shortened URL.
        """
        letters = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        end = (''.join(random.choice(letters) for letter in range(6)))
        url = 'http://tinyurl.com/'.join(end)
        urldict[end] = longUrl
        return url
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        end = ("http://tinyurl.com/4e9iAk").split('com/')[1]
        if end in urldict.keys(): return urldict[end]
        else: return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))








