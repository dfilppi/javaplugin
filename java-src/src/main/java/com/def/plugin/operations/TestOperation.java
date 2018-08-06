package com.def.plugin.operations;

import com.def.plugin.Context;

public class TestOperation implements Operation {

	public void execute(int ctx_port, String[] args) throws Exception{
		Context ctx = new Context(ctx_port);

		ctx.call_context("logger","info","HELLO WORLD");
		ctx.call_context("instance","runtime_properties","some_prop","some_val");
		String resp = ctx.call_context("instance", "runtime_properties", "some_prop", "some_val");
		ctx.call_context("logger","info","GOT RESP:", resp);
	}

}
