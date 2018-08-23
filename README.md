## javaplugin

An example/template implementation of a Cloudify plugin written in Java.

This example plugin is meant to be a starting point for those interested in developing Cloudify plugins in Java.  There are some simplifying assumptions:

* the Java code is contained in an executable jar package in the plugin directory named "plugin.jar"
* cloudify operations are implemented in the Java project as instances of Operation implementations.  These are referenced by class name in the plugin.yaml operations mapping.
* there is a little framework code in Java to bridge to the Cloudify context.
* the Cloudify context is accessed from Java using the context proxy, similar to the script plugin.  This means all strings in and out.
* it is assumed that the target platform already has Java installed.
* the result from the Context object is a JSON formatted string.  The example shows parsing it for values.

### Example

To run the example, you just need a Cloudify CLI ( `pip install cloudify`):
* install a java jdk
* cd to the example directory
* run `cfy init -r local-blueprint.yaml --install-plugins`
* run `cfy exe start install -b <directory>`

The example just shows the operation calling the Java code, and accessing the proxy object to set a runtime property and use Cloudify logging.

To rebuild the java jar, install Apache Maven, and run 'mvn package'.  The resulting _target/*jar-with-dependencies.jar_ file can be renamed 'plugin.jar' and placed in the plugin package.
