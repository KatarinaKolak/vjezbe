package rest_api;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import com.fasterxml.jackson.core.JsonProcessingException;
import org.springframework.stereotype.Component;
import org.springframework.web.context.annotation.RequestScope;

@Component
@RequestScope
public class MqttPublisher {
	private String clientID = "myClient";
	private MqttClient sampleClient;
	 
	public void publish(Message message) throws MqttException, InterruptedException, JsonProcessingException {
		MemoryPersistence persistence = new MemoryPersistence();
		sampleClient = new MqttClient(message.getBroker(), clientID, persistence);
		
		try {
			MqttConnectOptions connOpts = new MqttConnectOptions();
			connOpts.setCleanSession(true);
			sampleClient.connect(connOpts);

			MqttMessage mes = new MqttMessage(message.getMessage().getBytes());
			mes.setQos(2);
			sampleClient.publish(message.getTopic(), mes);
			
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
