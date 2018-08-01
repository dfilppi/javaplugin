from cloudify.decorators import operation
from cloudify.exceptions import NonRecoverableError
from cloudify import ctx
from cloudify.proxy.server import HTTPCtxProxy
import os
import json
import subprocess
import tempfile



def init(**kwargs):
#  """ download jars as need and put in classpath
#  """
#  dirname = tempfile.mkdtemp(prefix = "javaplugin")
#  classpath = os.environ['CLASSPATH'] if 'CLASSPATH' in os.environ else ""
#  ctx.logger.info("HERE")
#  jardir = os.path.dirname(os.path.abspath(__file__))+"/jars"
#  for dirpath,_,filenames in os.walk(jardir):
#    for f in filenames:
#      classpath += ":" + os.path.abspath(os.path.join(dirpath, f))
#  ctx.instance.runtime_properties['classpath'] = classpath

##
## Plugin operations
##
def calljava( opclass, args , **kwargs):
  """ Should do whatever "create" is defined as in java code.  It is assumed
      that the java implementation main function accepts an Operation class name and
      a varargs list
  """
  init()
  proxy_server = HTTPCtxProxy(ctx._get_current_object())
  
  try:
    # below will fail on windows
    #os.environ['CLASSPATH'] = ctx.instance.runtime_properties['classpath']
    res = subprocess.call([ "java" , "-jar", arpath, str(proxy_server.port), opclass, json.dumps( args )])
    if res !=0 :
      raise NonRecoverableError("func {} execution faild".format(func))
  finally:
    proxy_server.close()
