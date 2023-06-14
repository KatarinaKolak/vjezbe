package model;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Sensor {
	private String name;
	private String type;
	private int factor;
	private double min;
	private double max;
	private double value;
	private String unit;

	@JsonCreator
	public Sensor(@JsonProperty("name") String name, @JsonProperty("type") String type,
			@JsonProperty("factor") int factor, @JsonProperty("min") double minValue,
			@JsonProperty("max") double maxValue, @JsonProperty("unit") String unit) {
		this.name = name;
		this.type = type;
		this.factor = factor;
		this.min = minValue;
		this.max = maxValue;
		this.unit = unit;
	}
	
	public void setName(String name) {
		this.name = name;
	}

	public void setType(String type) {
		this.type = type;
	}

	public void setFactor(int factor) {
		this.factor = factor;
	}

	public void setMin(double min) {
		this.min = min;
	}

	public void setMax(double max) {
		this.max = max;
	}

	public void setValue(double value) {
		this.value = value;
	}

	public void setUnit(String unit) {
		this.unit = unit;
	}

	public String getName() {
		return this.name;
	}

	public String getType() {
		return this.type;
	}

	public int getFactor() {
		return this.factor;
	}

	public double getValue() {
		return this.value;
	}

	public double getMin() {
		return this.min;
	}

	public double getMax() {
		return this.max;
	}

	public String getUnit() {
		return this.unit;
	}

	public void generateRandomValue() {
		this.value = (double) ((Math.random() * (max - min)) + min);
	}
}
