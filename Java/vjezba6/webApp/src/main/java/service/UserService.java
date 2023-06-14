package service;

import model.MqttBroker;
import model.User;

public interface UserService {
    void save(User user);

    User findByUsername(String username);
    
    User findById(long id);
    
}