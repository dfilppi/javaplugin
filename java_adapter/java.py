from cloudify.decorators import operation
from cloudify.exceptions import NonRecoverableError
from cloudify import ctx
from cloudify.proxy.server import HTTPCtxProxy
import os
import json
import subprocess
import tempfile




##
## Plugin operations
##
def calljava( opclass, args , **kwargs):
  """ Should do whatever "create" is defined as in java code.  It is assumed
      that the java implementation main function accepts an Operation class name and
      a varargs list
  """
  proxy_server = HTTPCtxProxy(ctx._get_current_object())
  
  try:
    jarpath = os.path.dirname(os.path.abspath(__file__))+"/plugin.jar"
    # below will fail on windows
    res = subprocess.call([ "java" , "-jar", jarpath, str(proxy_server.port), opclass ]+args)
    if res !=0 :
      raise NonRecoverableError("operation {} execution failed".format(opclass))
  finally:
    proxy_server.close()
