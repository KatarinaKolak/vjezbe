package repository;

import org.springframework.data.jpa.repository.JpaRepository;
import model.MqttBroker;
import model.User;

public interface MqttBrokerRepository extends JpaRepository<MqttBroker, Long> {
    MqttBroker findByAddress(String address);
    MqttBroker findByPort(int port);
    MqttBroker findByUser(User user);
    MqttBroker findById(long id);
}