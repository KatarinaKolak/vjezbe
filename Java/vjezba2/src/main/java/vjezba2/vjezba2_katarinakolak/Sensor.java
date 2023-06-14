package vjezba2.vjezba2_katarinakolak;

public class Sensor {
	private String name;
	private String type;
	private int factor;
	private double min;
	private double max;
	private double value;
	private String unit;

	public Sensor(String name, String type, int factor, double minValue, double maxValue, String unit) {
		this.name = name;
		this.type = type;
		this.factor = factor;
		this.min = minValue;
		this.max = maxValue;
		generateRandomValue();
		if (this.factor != 0) {
			this.value = this.value / this.factor;
		}
		this.unit = unit;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getName() {
		return this.name;
	}

	public void setType(String dataType) {
		this.type = dataType;
	}

	public String getType() {
		return this.type;
	}

	public void setFactor(int factor) {
		this.factor = factor;
	}

	public int getFactor() {
		return this.factor;
	}

	public void setValue(double value) {
		this.value = value;
	}

	public double getValue() {
		return this.value;
	}

	public void setMin(double min) {
		this.min = min;
	}

	public void setMax(double max) {
		this.max = max;
	}

	public double getMin() {
		return this.min;
	}

	public double getMax() {
		return this.max;
	}

	public void setUnit(String measuringUnit) {
		this.unit = measuringUnit;
	}

	public String getUnit() {
		return this.unit;
	}

	public void generateRandomValue() {
		this.value = (double) ((Math.random() * (max - min)) + min);
	}

	public String getData() {
		return this.getName() + ": " + String.format("%.2f", this.getValue()) + " " + this.getUnit();
	}

	@Override
    public String toString() {
        return "Sensor [name = " + this.getName() + ", type = " + this.getType() + ", factor = " + this.getFactor()
                + ", min = " + this.getMin() + ", max = " + this.getMax() + ", value = " + this.getValue() + ", unit = " + this.getUnit() +  "]";
    }
	
}
