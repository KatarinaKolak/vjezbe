package MQTT;

import org.eclipse.paho.client.mqttv3.MqttException;

import vjezba2.vjezba2_katarinakolak.WaterFlowMeter;

public class MqttPublisher {

	public static void main(String[] args) throws MqttException, InterruptedException {

		WaterFlowMeter waterflow = new WaterFlowMeter();
		waterflow.publish();
	}
}