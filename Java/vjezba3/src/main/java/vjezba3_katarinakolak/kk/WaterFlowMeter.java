package vjezba3_katarinakolak.kk;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;

public class WaterFlowMeter {
	private String topic;
	private String broker;
	private String clientId;
	private List<Sensor> sensors = new ArrayList<>();

	@JsonCreator
	public WaterFlowMeter(@JsonProperty("topic") String topic, @JsonProperty("broker") String broker,
			@JsonProperty("clientId") String clientId, @JsonProperty("sensors") List<Sensor> sensors) {
		this.topic = topic;
		this.broker = broker;
		this.clientId = clientId;
		this.sensors = sensors;
	}

	public static WaterFlowMeter create(String path) throws IOException {
		ObjectMapper mapper = new ObjectMapper();
		mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
		WaterFlowMeter meter = mapper.readValue(Paths.get(path).toFile(), WaterFlowMeter.class);
		return meter;
	}

	public String toJson(Sensor sensor) throws JsonProcessingException {
		ObjectMapper objectMapper = new ObjectMapper();
		String value = objectMapper.writeValueAsString(sensor);
		return value;
	}

	public void publish() throws MqttException, InterruptedException, JsonProcessingException {
		MemoryPersistence persistence = new MemoryPersistence();
		@SuppressWarnings("resource")
		MqttClient sampleClient = new MqttClient(this.broker, this.clientId, persistence);

		while (true) {
			try {
				MqttConnectOptions connOpts = new MqttConnectOptions();
				connOpts.setCleanSession(true);
				sampleClient.connect(connOpts);
				for (Sensor sensor : sensors) {
					sensor.generateRandomValue();
					String content = toJson(sensor);
					System.out.println("Publishing message: " + content);
					MqttMessage message = new MqttMessage(content.getBytes());
					message.setQos(2);
					sampleClient.publish(topic, message);
				}
				System.out.println("\n");
				Thread.sleep(5000);
				sampleClient.disconnect();
			} catch (MqttException me) {
				System.out.println("reason " + me.getReasonCode());
				System.out.println("msg " + me.getMessage());
				System.out.println("loc " + me.getLocalizedMessage());
				System.out.println("cause " + me.getCause());
				System.out.println("excep " + me);
				me.printStackTrace();
			}
		}
	}
}
