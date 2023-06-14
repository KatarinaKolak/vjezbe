package vjezba3_katarinakolak.kk;

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
		generateRandomValue();
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
