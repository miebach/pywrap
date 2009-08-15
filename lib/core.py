import os

def is_unixy():
  """determine if the os behaves like unix avoiding sys.platform or os.name"""
  if os.path.join("a","b") == 'a/b':
    return 1
  return 0


