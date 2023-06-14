package service;

import model.MqttBroker;
import model.User;

public interface MqttBrokerService {
	 void save(MqttBroker broker);
	 MqttBroker findByAddress(String address);
	 MqttBroker findByPort(int port);
	 MqttBroker findByUser(User user);
	 MqttBroker findById(long id);
}
