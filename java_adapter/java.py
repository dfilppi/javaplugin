########
# Copyright (c) 2019 Cloudify Platform Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
############


from cloudify.exceptions import NonRecoverableError
from cloudify import ctx
from cloudify.proxy.server import HTTPCtxProxy
import os
import subprocess


##
# Plugin operations
##
def calljava(opclass, args, **kwargs):
    """ Should do whatever "create" is defined as in java code.  It is assumed
        that the java implementation main function accepts an Operation class
        name and a varargs list
    """
    proxy_server = HTTPCtxProxy(ctx._get_current_object())

    try:
        jarpath = os.path.dirname(os.path.abspath(__file__))+"/plugin.jar"
        # below will fail on windows
        res = subprocess.call(
            ["java", "-jar", jarpath, str(proxy_server.port), opclass]+args)
        if res != 0:
            raise NonRecoverableError(
                "operation {} execution failed".format(opclass))
    finally:
        proxy_server.close()
