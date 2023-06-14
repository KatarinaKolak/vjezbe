package model;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;

public class WaterFlowMeter {
	private String address;
	public String method;
	private List<Sensor> sensors = new ArrayList<>();

	@JsonCreator
	public WaterFlowMeter(@JsonProperty("address") String address, @JsonProperty("sensors") List<Sensor> sensors, 
			@JsonProperty("method") String method) {
		this.address = address;
		this.method = method;
		this.sensors = sensors;
	}

	public void setBAddress(String broker) {
		this.address = broker;
	}

	public String getMethod() {
		return method;
	}

	public void setMethod(String method) {
		this.method = method;
	}
	
	public void setSensors(List<Sensor> sensors) {
		this.sensors = sensors;
	}

	public String getAddress() {
		return this.address;
	}

	public List<Sensor> getSensors() {
		return this.sensors;
	}

	public Sensor getSensor(int i) {
		return sensors.get(i);
	}
	

	public void publish() throws InterruptedException, IOException{
		Publisher publisher = new Publisher(method, address, sensors);
	}
	
	public static WaterFlowMeter create(String path) throws IOException {
		ObjectMapper mapper = new ObjectMapper();
		mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
		WaterFlowMeter meter = mapper.readValue(Paths.get(path).toFile(), WaterFlowMeter.class);
		return meter;
	}

}
