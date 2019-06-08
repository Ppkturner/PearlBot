import re
import itertools

def zip_str(a, b):
	return [(c, '') if d is None else ('', d) if c is None else (c, d) for c,d in itertools.zip_longest(a,b)]
	
def findPer(string):
	pattern = '((p[eu]+r)+(?![aeiou]+))'
	patternRegEx = re.compile(pattern, re.IGNORECASE)# + re.DEBUG)
	return re.sub(patternRegEx, lambda x: '***{0}***'.format(''.join(d.upper() if c.isupper() else d.lower() for c,d in zip_str(x.group(), 'pearl'))), string)