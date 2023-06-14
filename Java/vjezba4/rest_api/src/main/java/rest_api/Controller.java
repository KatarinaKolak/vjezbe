package rest_api;

import org.eclipse.paho.client.mqttv3.MqttException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.fasterxml.jackson.core.JsonProcessingException;

import org.springframework.http.MediaType;

import java.security.Principal;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
public class Controller {
	@Autowired
	private MqttPublisher mqttPublisher;
	  
	@PostMapping(value = "/message", consumes = MediaType.APPLICATION_JSON_VALUE)
	public void createWaterFlowMeter(@RequestBody Message message) throws JsonProcessingException, MqttException, InterruptedException  {
		mqttPublisher.publish(message);
	}
}
