package com.cloudify.plugin;

import java.util.Arrays;

import com.cloudify.plugin.operations.Operation;

/**
 * Hello world!
 *
 */
public class Plugin 
{
    public static void main( String[] args )throws Exception
    {
        int ctx_port = Integer.valueOf(args[0]);
        String opname = args[1];
        String[] parms = Arrays.copyOfRange(args, 2, args.length-1);
        
        Operation op = (Operation)Class.forName(opname).newInstance();
        op.execute(ctx_port, parms);
             
    }
}
