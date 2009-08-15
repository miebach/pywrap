""" 
# wrappers for processes 
  
## environment
 
- processes have environments that consist of key-value pairs
- every new process inherits the environment at the time of it's creation,
  but after that each environment is independent.

## ways to maniplate processes

### os.system

- simple but no control over the process  

### exec-

- use this on unix-like platforms only, because it uses fork

### spwan- and popen-

- cross-platform
- intermediate simplicity and power



## files or shell-commands?

### RUN a FILE

exec and spwan

### Pass a CMD-STRING to a SHELL

system and popen

"""

import os
import lib.editcore as editcore

def call(cmd,more_lines=[]):
  """
  executes the commandline cmd as a new process p and passes more_lines (which must be a list of lines)
  as input to p. returns p's output as a list of lines.
  """

  fi,fo = os.popen2(cmd,'t')
  for l in  more_lines:
    fi.write(l+"\n")
  fi.close()
  rescr = fo.readlines()
  # remove the trailing newline chracters from the resulting lines:
  res = []
  for l in rescr:
    res.append(editcore.rtrim_crlf(l))
  fo.close()
  return res


def established_by_port(port):
  # returns a list of processes with established connections on the port
  cmd = "lsof -i :%s|grep ESTABLISHED" % port
  res = call(cmd)
  return res

def kill(process_list=[]):
  # kill all processes by pids in the list
  for p in process_list:
    call("kill %s" % p)





