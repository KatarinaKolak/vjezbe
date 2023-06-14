package model;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;

@Component
public class MqttSubscriber implements MqttCallback  {
	/** The client id. */
	private static final String clientId = "clientId";
	private MqttClient sampleClient;
	private static final List<String> messages = new ArrayList<>();


	/** The topic. */
	//private static final String topic = "test";

	public void subscribe(String topic, String address, int port) {
		//	logger file name and pattern to log
		MemoryPersistence persistence = new MemoryPersistence();
		String brokerUrl = address + ":" + Integer.toString(port);
		try
		{

			sampleClient = new MqttClient(brokerUrl, clientId, persistence);
			MqttConnectOptions connOpts = new MqttConnectOptions();
			connOpts.setCleanSession(true);

			System.out.println("checking");
			System.out.println("Mqtt Connecting to broker: " + brokerUrl);

			sampleClient.connect(connOpts);
			System.out.println("Mqtt Connected");

			sampleClient.setCallback(this);
			sampleClient.subscribe(topic);

			System.out.println("Subscribed");
			System.out.println("Listening");

		} catch (MqttException me) {
			System.out.println(me);
		}
	}

	 //Called when the client lost the connection to the broker
	public void connectionLost(Throwable arg0) {
		
	}

	//Called when a outgoing publish is complete
	public void deliveryComplete(IMqttDeliveryToken arg0) {

	}

	public void messageArrived(String topic, MqttMessage message) throws Exception {

		System.out.println("| Topic:" + topic);
		System.out.println("| Message: " +message.toString());
		System.out.println("-------------------------------------------------");
		messages.add(new String(message.getPayload()));
	}
	
	public List<String> getMessages() {
		return messages;
	}
	
	public void disconnect() {
		try {
			messages.clear();
			sampleClient.disconnect();
			System.out.println("Disconnected!");
		} catch (MqttException me) {
			me.printStackTrace();
		}
	}

}
