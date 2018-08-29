package com.cloudify.plugin.operations;

public interface Operation {
	
	void execute(int ctx_port, String [] args) throws Exception;

}
