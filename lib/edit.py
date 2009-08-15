import lib.core as core
import lib.editcore as editcore
import lib.act as act

def cut(lines=[],params=""):
  """call the cut command on unix-like systems"""
  if not core.is_unixy():
    raise("cut is only implemented on unix-like systems")
  cmd = "cut"
  if params != "":
    cmd = cmd + " " + params
  res = act.call(cmd,lines)
  return res
 
def cut_by(code,lines=[],nfrom=None,nto=None,complement=0):
  list = editcore.create_cut_list(nfrom,nto)
  params = "%s %s" % (code,list)
  if complement:
    params = params + " --complement"
  res = cut(lines,params)
  return res

def cut_bytes(lines=[],nfrom=None,nto=None,complement=0):
 """the bytes version of the cut command"""
 return cut_by("-b",lines,nfrom,nto,complement) 

def cut_byte(lines,n,complement=0):
  """only 1 byte"""
  return cut_bytes(lines,n,n,complement) 



def cut_fields(lines=[],nfrom=None,nto=None,complement=0):
  """the fields version of the cut command"""
  return cut_by("-f",lines,nfrom,nto,complement) 

def cut_field(lines,n,complement=0):
  """only 1 field"""
  return cut_fields(lines,n,n,complement) 



def cut_characters(lines=[],nfrom=None,nto=None,complement=0):
  """the chars version of the cut command"""
  return cut_by("-c",lines,nfrom,nto,complement) 





