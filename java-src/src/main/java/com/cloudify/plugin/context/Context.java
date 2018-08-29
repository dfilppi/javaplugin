package com.cloudify.plugin.context;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;

public class Context {
	
	private int port;

	public Context(int port) {
		this.port=port;
	}

	public String call_context( String ...args) throws IOException {
		//Setup connection to context
		URL url = new URL("http://localhost:"+ port);
		URLConnection con = url.openConnection();
		HttpURLConnection http = (HttpURLConnection)con;
		http.setRequestMethod("POST"); // PUT is another valid option
		http.setDoInput(true);
		http.setDoOutput(true);		

		StringBuilder sb = new StringBuilder("{\"args\": [ ");
		for(String arg:args) {
			arg = arg.replaceAll("\"", "\\\\\\\"");
			arg = arg.replaceAll("\\n", "");
			sb.append("\"").append(arg).append("\",");
		}
		sb.deleteCharAt(sb.length()-1);
		sb.append("] }");

		//POST request
		http.setFixedLengthStreamingMode(sb.length());
		http.setRequestProperty("Content-Type", "application/json; charset=UTF-8");
		http.connect();

		OutputStream os = http.getOutputStream();
		os.write(sb.toString().getBytes());
		os.flush();
		os.close();

		// Read response
		StringBuilder content;

		BufferedReader in = new BufferedReader(
				new InputStreamReader(http.getInputStream()));

		String line;
		content = new StringBuilder();

		while ((line = in.readLine()) != null) {
			content.append(line);
			content.append(System.lineSeparator());
		}
		in.close();
		
		return content.toString();
	}

}
