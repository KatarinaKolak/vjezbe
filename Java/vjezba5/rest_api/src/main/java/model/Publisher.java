package model;
import java.util.List;

public class Publisher {
	public Publisher(String method, String address, List<Sensor> sensors) {
		rest_api.Publisher publisher = MethodFactory.create(method, address, sensors);
		if (publisher != null) {
			publisher.publish();
		}
	}
}
