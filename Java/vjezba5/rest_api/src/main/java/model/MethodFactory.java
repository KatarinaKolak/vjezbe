package model;

import java.util.List;
import rest_api.MQTTPublisher;
import rest_api.Publisher;
import rest_api.HTTPPublisher;

public class MethodFactory{
	
	public static Publisher create(String method, String address, List<Sensor> sensors) {
		if (method.equalsIgnoreCase("mqtt")) {
			return new MQTTPublisher(address, sensors);
		}else if (method.equalsIgnoreCase("http")) {
			return new HTTPPublisher(address, sensors);
		}else {
			System.out.println("Not found!");
			return null;
		}
	}
}
