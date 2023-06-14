package rest_api;

import java.net.ProxySelector;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpResponse.BodyHandlers;
import java.util.List;
import java.io.IOException;
import java.net.InetSocketAddress;

import com.google.gson.*;

import model.Sensor;

public class HTTPPublisher implements Publisher {
	private HttpClient client;
	public HttpRequest request;
	private String address;
	private Gson gson = new Gson();
	private List<Sensor> sensors;
	
	public HTTPPublisher(String address, List<Sensor> sensors) {
		this.address = address;
		this.sensors = sensors;
		this.client = HttpClient.newBuilder()
				.version(HttpClient.Version.HTTP_2)
				.followRedirects(HttpClient.Redirect.ALWAYS)
				.proxy(ProxySelector.of(new InetSocketAddress("www-proxy.com", 8080)))
				.build();
	}
		
	@Override
	public void publish() {
		for (Sensor sensor : sensors) {
			String data = gson.toJson(sensor);
			
			this.request = HttpRequest.newBuilder()
						.uri(URI.create(this.address))
						.header("Content-Type", "application/json")
						.POST(HttpRequest.BodyPublishers.ofString(data))
						.build();
			
			try {
				HttpResponse<String> send = this.client.send(request, BodyHandlers.ofString());
				System.err.println("Response code: " + send.statusCode());
			} catch (IOException e) {
				e.printStackTrace();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}
