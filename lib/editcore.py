CR="\r"
LF="\n"

def rtrim_crlf(s):
  """ remove any cr or lf character from the end of the s """
  if s == None:
    return s
  while 1:
    if len(s) == 0:
      return s
    if s[-1:] in [CR,LF]:
      s = s[:-1]
    else:
      return s

def create_cut_list(nfrom,nto):
  if (nfrom is None) and (nto is None):
    raise("nfrom and nto cannot both be None")
  if nfrom == nto:
    list = "%s" % nfrom
  elif nfrom is None:
     list="-%s" % nto
  elif nto is None:
     list="%s-" % nfrom
  else:
     list="%s-%s" % (nfrom,nto)
  return list
  
 
  

