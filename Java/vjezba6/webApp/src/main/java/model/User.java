package model;

import javax.persistence.*;

@Entity
@Table(name = "user_entity")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String username;
    private String password;

    @Transient
    private String passwordConfirm;

    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "broker_id", referencedColumnName = "id")
    private MqttBroker broker;

	public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getPasswordConfirm() {
        return passwordConfirm;
    }

    public void setPasswordConfirm(String passwordConfirm) {
        this.passwordConfirm = passwordConfirm;
    }
    
    public MqttBroker getBroker() {
  		return broker;
  	}

  	public void setBroker(MqttBroker broker) {
  		this.broker = broker;
  	}
}