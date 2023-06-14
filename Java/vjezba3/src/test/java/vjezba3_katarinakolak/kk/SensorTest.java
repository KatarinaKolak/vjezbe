package vjezba3_katarinakolak.kk;

import static org.junit.Assert.*;

import org.junit.Test;

public class SensorTest {

	@Test
	public void getName_InputNone_OutputSensorName() {
		Sensor givenSensor = new Sensor("newSensor", "int16", 1000, 0, 65.336, "Bar");
		String expectedName = "newSensor";

		String result = givenSensor.getName();

		assertEquals(expectedName, result);
	}

	@Test
	public void getType_InputNone_OutputDataType() {
		Sensor givenSensor = new Sensor("newSensor", "int16", 1000, 0, 65.336, "Bar");
		String expectedType = "int16";

		String result = givenSensor.getType();

		assertEquals(expectedType, result);
	}

	@Test
	public void getFactor_InputNone_OutputFactor() {
		Sensor givenSensor = new Sensor("newSensor", "int16", 1000, 0, 65.336, "Bar");
		int expectedFactor = 1000;

		int result = givenSensor.getFactor();

		assertEquals(expectedFactor, result);
	}

	@Test
	public void getUnit_InputNone_OutputMeasuringUnit() {
		Sensor givenSensor = new Sensor("newSensor", "int16", 1000, 0, 65.336, "Bar");
		String expectedUnit = "Bar";

		String result = givenSensor.getUnit();

		assertEquals(expectedUnit, result);
	}

	@Test
	public void getMin_InputNone_OutputMinValue() {
		Sensor givenSensor = new Sensor("newSensor", "int16", 1000, 0.0, 65.336, "Bar");
		double expectedMin = 0.0;

		double result = givenSensor.getMin();

		assertEquals(expectedMin, result, 1e-7);
	}

	@Test
	public void getMax_InputNone_OutputMaxValue() {
		Sensor givenSensor = new Sensor("newSensor", "int16", 1000, 0.0, 65.336, "Bar");
		double expectedMax = 65.336;

		double result = givenSensor.getMax();

		assertEquals(expectedMax, result, 1e-7);
	}
}
