## goplugin

An example/template implementation of a Cloudify plugin written in Go.

This example plugin is meant to be a starting point for those interested in developing Cloudify plugins in Go.  There are some simplifying assumptions:

* the Go code is stored in the plugin module under `golang_adapter/src`
* an executable is built on first reference
* cloudify operations are multiplexed through a single Python adapter function in 'golang_adapter/go.py`.  The Go implemented operates are selected by inputs on the operations
* there is a little framework code in Go to multiplex the operation request, and to bridge to the Cloudify context.
* the Cloudify context is accessed from Go using the context proxy, similar to the script plugin.  This means all strings in and out.
* the actual implementations in the example are in the `golang_adapter\src\plugin\operation.go` file.
* it is assumed that the target platform already has Go installed.
* it is left as an exercise for the implementor the parse the JSON return value from the context proxy

### Example

To run the example, you just need a Cloudify CLI ( `pip install cloudify`):
* install Go
* cd to the example directory
* run `cfy init -r local-blueprint.yaml --install-plugins`
* run `cfy exe start install -b goplugin`

The example just shows the operation calling the Go code, and accessing the proxy object to set a runtime property and use Cloudify logging.
