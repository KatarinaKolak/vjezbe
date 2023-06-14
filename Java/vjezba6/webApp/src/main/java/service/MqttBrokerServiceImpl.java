package service;

import model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import model.MqttBroker;
import repository.MqttBrokerRepository;

@Component
@Service
public class MqttBrokerServiceImpl implements MqttBrokerService{
	@Autowired
    private MqttBrokerRepository brokerRepository;
	
    public void save(MqttBroker broker) {
   
        brokerRepository.save(broker);
    }

    public MqttBroker findByAddress(String address) {
        return brokerRepository.findByAddress(address);
    }
    
    public MqttBroker findByPort(int port) {
        return brokerRepository.findByPort(port);
    }
    
    public MqttBroker findByUser(User user) {
        return brokerRepository.findByUser(user);
    }
    
    public MqttBroker findById(long id){
        return brokerRepository.findById(id);
    }
}
