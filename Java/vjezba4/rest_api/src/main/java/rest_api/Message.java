package rest_api;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Message {
	private String topic;
	private String broker;
	private String message;

	@JsonCreator
	public Message(@JsonProperty("topic") String topic, @JsonProperty("broker") String broker,
			@JsonProperty("message") String message) {
		this.topic = topic;
		this.broker = broker;
		this.message = message;
	}

	public String getTopic() {
		return topic;
	}

	public void setTopic(String topic) {
		this.topic = topic;
	}

	public String getBroker() {
		return broker;
	}

	public void setBroker(String broker) {
		this.broker = broker;
	}

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}

}
