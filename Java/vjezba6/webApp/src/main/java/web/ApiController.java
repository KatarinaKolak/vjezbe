package web;

import model.User;
import service.SecurityService;
import service.UserService;
import model.MqttBroker;
import model.MqttSubscriber;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import java.security.Principal;
import model.Topic;

@Controller
public class ApiController {
    @Autowired
    private UserService userService;

    @Autowired
    private SecurityService securityService;

    @Autowired
    private MqttSubscriber subscriber;

    @Autowired
    private UserValidator userValidator;

    @GetMapping("/registration")
    public String registration(Model model) {
        if (securityService.isAuthenticated()) {
            return "redirect:/";
        }

        if (!subscriber.getMessages().isEmpty()) {
			subscriber.disconnect();
		}

        model.addAttribute("userForm", new User());

        return "registration";
    }

    @PostMapping("/registration")
    public String registration(Model model, String error, @ModelAttribute("userForm") User userForm, BindingResult bindingResult) {
        userValidator.validate(userForm, bindingResult);

        if (bindingResult.hasErrors()) {
            return "registration";
        }

        
        if (error != null)
            model.addAttribute("error", "Your username and password is invalid.");

        userService.save(userForm);

        securityService.autoLogin(userForm.getUsername(), userForm.getPasswordConfirm());

        return "redirect:/mqttConfig";
    }

    @GetMapping("/mqttConfig")
    public String mqttConfiguration(Model model) { 	
    	if (!securityService.isAuthenticated()) {
			return "redirect:/login";
		}
    	
    	if (!subscriber.getMessages().isEmpty()) {
			subscriber.disconnect();
		}
    	
        model.addAttribute("brokerForm", new MqttBroker());

        return "mqttConfig";
    }

    @PostMapping("/mqttConfig")
    public String mqttConfiguration(Principal principal, @ModelAttribute("brokerForm") MqttBroker brokerForm, BindingResult bindingResult) {
        if (bindingResult.hasErrors()) {
            return "mqttConfig";
        }

        User user = userService.findByUsername(principal.getName());
		user.setBroker(brokerForm);
		userService.save(user);
		 
        return "redirect:/topic";
    }
    
    @GetMapping("/subscribe")
	public String subscribe(Principal principal, Model model) {
		if (!securityService.isAuthenticated()) {
			return "redirect:/login";
		}
		
		model.addAttribute("messages", subscriber.getMessages());

		return "subscribe";
	}
    
    @GetMapping("/topic")
	public String topicConfig(Principal principal, Model model) {
		if (!securityService.isAuthenticated()) {
			return "redirect:/login";
		}
		
		if (!subscriber.getMessages().isEmpty()) {
			subscriber.disconnect();
		}
		
		model.addAttribute("topicForm", new Topic());
		
		return "topic";
	}
    
    @PostMapping("/topic")
  	public String topicConf(Principal principal, Model model, @ModelAttribute("topicForm") Topic topicForm, BindingResult bindingResult) {
  		if (!securityService.isAuthenticated()) {
  			return "redirect:/login";
  		}
  		
  		User user = userService.findByUsername(principal.getName());
  		
  		subscriber.subscribe(topicForm.getTopic(), user.getBroker().getAddress(), user.getBroker().getPort());
  		
  		return "redirect:/subscribe";
  	}
    
    @GetMapping({"/", "/login"})
    public String login(Model model, String error, String logout) {
        if (securityService.isAuthenticated()) {
            return "redirect:/mqttConfig";
        }
        
        if (!subscriber.getMessages().isEmpty()) {
			subscriber.disconnect();
		}

        if (error != null)
            model.addAttribute("error", "Your username and password is invalid.");

        if (logout != null)
            model.addAttribute("message", "You have been logged out successfully.");

        return "login";
    }
}