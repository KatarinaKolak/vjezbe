package vjezba1;

public class Color {
	private int red;
	private int blue;
	private int green;
	
	public Color(int r, int g, int b) {
		this.red = r;
		this.green = g;
		this.blue = b;
	}
	public int getRed() {
		return this.red;
	}
	public int getGreen() {
		return this.green;
	}
	public int getBlue() {
		return this.blue;
	}
	public int getRGB() {
		return ((this.getRed() << 16) | (this.getGreen() << 8) | this.getBlue());
	}
	public static Color decode(String nm) {
		int i = Integer.decode(nm);
		return new Color((i >> 16) & 0xFF, (i >> 8) & 0xFF, i & 0xFF);
	}
	public static float[] RGBtoHSB(int r, int g, int b, float[] hsbvals) {
		float red = r / 255.0f;
		float green = g / 255.0f;
		float blue = b / 255.0f;

		float max = Math.max(red, green);
		max = Math.max(max, blue);
		hsbvals[2] = max;

		float min = Math.min(red, green);
		min = Math.min(min, blue);

		if (max == 0) {
			hsbvals[1] = 0;
		} else {
			hsbvals[1] = (max - min)/ max;
		}

		if (max - min == 0) {
			hsbvals[0] = 0;
		} else if (red == max) {
			hsbvals[0] = (green - blue) / (max - min);
		} else if (green == max) {
			hsbvals[0] = 2.0f + (blue - red) / (max - min);
		} else if (blue == max) {
			hsbvals[0] = 4.0f + (red - green) / (max - min);
		}
		
		hsbvals[0] /= 6;
		
		if (hsbvals[0] < 0)
			hsbvals[0] += 360;
		
		return hsbvals;
	}
	public static float[] RGBtoHSL(int r, int g, int b, float[] hslvals) {
		float red = r / 255.0f;
		float green = g / 255.0f;
		float blue = b / 255.0f;

		float max = Math.max(red, green);
		max = Math.max(max, blue);

		float min = Math.min(red, green);
		min = Math.min(min, blue);
		hslvals[2] = (max + min) / 2;

		if ((max - min) == 0) {
			hslvals[1] = 0;
		} else {
			hslvals[1] = (max - min) / (1 - Math.abs(2*hslvals[2] - 1));
		}
		
		if (max - min == 0) {
			hslvals[0] = 0;
		} else if (red == max) {
			hslvals[0] = ((green - blue) / (max - min)) % 6;
		} else if (green == max) {
			hslvals[0] = 2.0f + (blue - red) / (max - min);
		} else if (blue == max) {
			hslvals[0] = 4.0f + (red - green) / (max - min);
		}
		
		if (hslvals[0] < 0)
			hslvals[0] += 360;
		
		return hslvals;
	}
	public static float[] RGBtoCMYK(int r, int g, int b, float[] cmykvals) {
		float red = r / 255.0f;
		float green = g / 255.0f;
		float blue = b / 255.0f;
		
		float max = Math.max(red, green);
		max = Math.max(max, blue);
		
		float k = 1 - max;
		cmykvals[0] = (1 - red - k) / (1-k);
		cmykvals[1] = (1 - green - k) / (1 - k);
		cmykvals[2] = (1 - blue - k) / (1 - k);
		cmykvals[3] = k;
		
		return cmykvals;
	}
}
