#!/usr/bin/env python
#-*- coding:utf-8 -*-
def response()
  with open('xss_solution.txt', 'w') as f:
    f.write('XSS Found!
solution suugest:
1. The encoding
HTML Entity encoding, or escape from, the data entered by the user.Against XSS, at least in the HTMLEncode <, >, &, ", "into & lt, & gt, & amp, & quot, & # 39, etc
2.Filter
Remove the DOM attributes uploaded by users, such as onerror, etc.Remove the Style node, Script node, iframe and so on uploaded by the user
3. The correction
Avoid decoding HTML Entity directly, and use the DOM Parse transform to correct mismatched DOM tags.
4. Secondary inspection
In addition to checking on the client side, a second check on the back end is often required.The main purpose of client checking is to block the majority of normal users who misoperate.')
