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
