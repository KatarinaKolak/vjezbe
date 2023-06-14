package vjezba1;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertTrue;

import org.junit.*;

public class ColorTest {

	@Test
	public void getRed_InputNone_OutputRed() {
		Color givenColor = new Color(40, 30, 255);
		int expectedRed = 40;
		int notExpectedRed = 32;

		int result = givenColor.getRed();

		assertEquals(expectedRed, result);
		assertNotEquals(notExpectedRed, result);
		assertTrue(notExpectedRed < result);
	}

	@Test
	public void getGreen_InputNone_OutputGreen() {
		Color givenColor = new Color(40, 30, 255);
		int expectedGreen = 30;
		int notExpectedGreen = 255;

		int result = givenColor.getGreen();

		assertEquals(expectedGreen, result);
		assertNotEquals(notExpectedGreen, result);
		assertTrue(notExpectedGreen > result);
	}

	@Test
	public void getBlue_InputNone_OutputBlue() {
		Color givenColor = new Color(40, 30, 255);
		int expectedBlue = 255;
		int notExpectedBlue = 34;

		int result = givenColor.getBlue();

		assertEquals(expectedBlue, result);
		assertNotEquals(notExpectedBlue, result);
		assertTrue(notExpectedBlue < result);
	}

	@Test
	public void getRGB_InputNone_OutputInt() {
		Color givenColor = new Color(40, 30, 255);
		int notExpectedRGB = 4030255;
		int expectedRGB = 2629375;

		int result = givenColor.getRGB();

		assertNotEquals(notExpectedRGB, result);
		assertEquals(expectedRGB, result);
	}

	@Test
	public void Decode_InputHex_OutputColor() {
		String givenHex = "0xFF0F00";
		int expectedRed = 255;
		int expectedGreen = 15;
		int expectedBlue = 0;

		Color result = Color.decode(givenHex);

		assertEquals(expectedRed, result.getRed());
		assertEquals(expectedGreen, result.getGreen());
		assertEquals(expectedBlue, result.getBlue());
		assertNotEquals(expectedRed, result.getBlue());
	}

	@Test
	public void RGBtoHSB_InputRGB_OutputHSB() {
		int givenRed = 45;
		int givenGreen = 220;
		int givenBlue = 250;
		float[] givenHSB = new float[3];
		float expectedBrightness = (float) 0.98039215;
		float[] expectedHSB = { (float) 0.5243902, (float) 0.82, (float) 0.98039215 };

		float[] result = Color.RGBtoHSB(givenRed, givenGreen, givenBlue, givenHSB);

		assertEquals(expectedHSB[0], result[0], 1e-7);
		assertEquals(expectedHSB[1], result[1], 1e-7);
		assertEquals(expectedHSB[2], result[2], 1e-7);
		assertEquals(result[2], expectedBrightness, 1e-7);
	}

	@Test
	public void RGBtoHSL_InputRGB_OutputHSL() {
		int givenRed = 45;
		int givenGreen = 220;
		int givenBlue = 250;
		float[] givenHSL = new float[3];
		float[] expectedHSL = { (float) 3.1463412385, (float) 0.95348834, (float) 0.5784313 };

		float[] result = Color.RGBtoHSL(givenRed, givenGreen, givenBlue, givenHSL);

		assertEquals(expectedHSL[0], result[0], 1e-7);
		assertEquals(expectedHSL[1], result[1], 1e-7);
		assertEquals(expectedHSL[2], result[2], 1e-7);
	}

	@Test
	public void RGBtoCMYK_InputRGB_OutputCMYK() {
		int givenRed = 45;
		int givenGreen = 220;
		int givenBlue = 250;
		float[] givenCMYK = new float[4];
		float[] expectedCMYK = { (float) 0.81999999, (float) 0.11999999, (float) 0.0, (float) 0.0 };

		float[] result = Color.RGBtoCMYK(givenRed, givenGreen, givenBlue, givenCMYK);

		assertEquals(expectedCMYK[0], result[0], 1e-7);
		assertEquals(expectedCMYK[1], result[1], 1e-7);
		assertEquals(expectedCMYK[2], result[2], 1e-7);
	}
}
