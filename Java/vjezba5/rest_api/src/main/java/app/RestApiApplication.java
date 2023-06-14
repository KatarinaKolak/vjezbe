package app;

import java.io.IOException;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.*;
import model.WaterFlowMeter;

@SpringBootApplication
@EnableAutoConfiguration
@ComponentScan ({"app", "model", "rest_api"})
public class RestApiApplication {

	public static void main(String[] args) throws IOException, InterruptedException {
		WaterFlowMeter waterflow = WaterFlowMeter.create("C:\\Users\\HP 255\\Documents\\workspace-spring-tool-suite-4-4.8.1.RELEASE\\rest_api\\src\\main\\java\\config\\config.json");
		
		waterflow.publish();
		
		SpringApplication.run(RestApiApplication.class, args);
	}
}
	
