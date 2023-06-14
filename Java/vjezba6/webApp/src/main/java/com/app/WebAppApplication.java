package com.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.*;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

@SpringBootApplication
@EnableAutoConfiguration
@ComponentScan ({"com.app", "service", "web", "repository", "model"})
@EntityScan("model")
@EnableJpaRepositories("repository")
public class WebAppApplication {
	public static void main(String[] args) {
		SpringApplication.run(WebAppApplication.class, args);
	}

}
