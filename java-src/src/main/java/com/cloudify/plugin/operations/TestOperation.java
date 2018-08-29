package com.cloudify.plugin.operations;

import com.cloudify.plugin.context.Context;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class TestOperation implements Operation {
	
	public static void main(String[] args) {
		
	}

	public void execute(int ctx_port, String[] args) throws Exception{
		Context ctx = new Context(ctx_port);

		ctx.call_context("instance","runtime_properties","some_prop","some_val");
		ctx.call_context("logger","info","set some_prop = some_val");
		String resp = ctx.call_context("instance", "runtime_properties", "some_prop");
		ObjectMapper mapper = new ObjectMapper();
		JsonNode root = mapper.readTree(resp);
		String val = root.findValue("payload").asText();
		ctx.call_context("logger","info","fetched some_prop = "+ val);
				
	}
	

}
