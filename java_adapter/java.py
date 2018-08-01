from cloudify.decorators import operation
from cloudify.exceptions import NonRecoverableError
from cloudify import ctx
from cloudify.proxy.server import HTTPCtxProxy
from functools import wraps
import os
import json
import subprocess
import tempfile


def init(jar, **kwargs):
  """ download jars as need and put in classpath
  """
  dirname = mkdtemp(prefix = "javaplugin")
  classpath = os.environ['CLASSPATH']
  for jar in jars:
    path = dirname+"/"+os.path.basename(jar)
    ctx.download_resource(jar, path)
    classpath += ":" + path
  ctx.instance.runtime_properties['classpath'] = classpath

##
## Plugin operations
##
def calljava( func, args , **kwargs):
  """ Should do whatever "create" is defined as in java code.  It is assumed
      that the java implementation main function accepts a funcion name and
      a varargs list
  """
  proxy_server = HTTPCtxProxy(ctx._get_current_object())
  
  try:
    jarpath = ctx.instance.runtime_properties['plugin_path']
    # below will fail on windows
    os.environ['CLASSPATH'] = ctx.instance.runtime_properties['classpath']
    res = subprocess.call([ "java" , "-jar", jarpath, str(proxy_server.port), func, json.dumps( args )])
    if res !=0 :
      raise NonRecoverableError("func {} execution faild".format(func))
  finally:
    proxy_server.close()
