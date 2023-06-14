package vjezba2.vjezba2_katarinakolak;

import java.util.ArrayList;
import java.util.List;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class WaterFlowMeter {
	private String topic = "waterflow";
	private int qos = 2;
	private String broker = "tcp://localhost:1883";
	private String clientId = "MqttClient";
	private List<Sensor> sensors = new ArrayList<>();
	
	public WaterFlowMeter() {
		this.sensors.add(new Sensor("Current water temperature", "int16", 10, -3266.8, 3266.8, "Celsius"));
		this.sensors.add(new Sensor("Current water pressure", "int16", 1000, 0, 65.336, "Bar"));
		this.sensors.add(new Sensor("Consumption in last 1 min, 10 min, 1 hour, 1 day ", "uint16", 0, 0, 65336, "Litra"));
		this.sensors.add(new Sensor("Consumption in last 1 week, 1 month, 1 year", "uint16", 10, 0, 6533.6, "m3"));
	}
	
	public void publish() throws MqttException, InterruptedException {
		MemoryPersistence persistence = new MemoryPersistence();
		@SuppressWarnings("resource")
		MqttClient sampleClient = new MqttClient(this.broker, this.clientId, persistence);

		while(true) {
			try {
				MqttConnectOptions connOpts = new MqttConnectOptions();
				connOpts.setCleanSession(true);
				sampleClient.connect(connOpts);
				for (Sensor sensor : sensors) {
					String content = sensor.getData();
					System.out.println("Publishing message: " + content);
					MqttMessage message = new MqttMessage(content.getBytes());
					message.setQos(qos);
					sampleClient.publish(topic, message);
					sensor.generateRandomValue();
					Thread.sleep(3000);
				}
				System.out.println("\n");
				Thread.sleep(4000);
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
