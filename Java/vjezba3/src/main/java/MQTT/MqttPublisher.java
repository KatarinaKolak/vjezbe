package MQTT;

import java.io.IOException;

import org.eclipse.paho.client.mqttv3.MqttException;

import vjezba3_katarinakolak.kk.WaterFlowMeter;

public class MqttPublisher {

	public static void main(String[] args) throws MqttException, InterruptedException, IOException {
		WaterFlowMeter waterflow = WaterFlowMeter.create("C:\\Users\\java\\myFile.json");
		waterflow.publish();
	}
}
