package rest_api;

import org.eclipse.paho.client.mqttv3.MqttClient;
import com.google.gson.*;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import java.util.List;
import model.Sensor;

public class MQTTPublisher implements Publisher {
	private String clientID = "myClient";
	private MqttClient sampleClient;
	private String broker;
	private List<Sensor> sensors;
	private Gson gson = new Gson();

	public MQTTPublisher(String address, List<Sensor> sensors) {
		this.broker = address;
		this.sensors = sensors;
		
		try {
			sampleClient = new MqttClient(broker, clientID);
		} catch (MqttException e) {
			e.printStackTrace();
		}
	}

	@Override
	public void publish() {
		MqttMessage mqttMessage = new MqttMessage();
		for (Sensor sensor : sensors) {
			String data = gson.toJson(sensor);
			mqttMessage.setPayload(data.getBytes());
			
			try {
				sampleClient.connect();
				String topic = "myTopic";
				sampleClient.publish(topic, mqttMessage);
				sampleClient.disconnect();
			} catch (MqttException me) {
				System.out.println("reason " + me.getReasonCode());
				System.out.println("msg " + me.getMessage());
				System.out.println("loc " + me.getLocalizedMessage());
				System.out.println("cause " + me.getCause());
				System.out.println("excep " + me);
				me.printStackTrace();
			}
			
			System.out.println("Data " + data);
		}
	}
}
