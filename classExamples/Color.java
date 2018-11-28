// An implementation of an RGB color
public class Color {
  private double red;
  private double green;
  private double blue;

  public Color(double red, double green, double blue)
  {
    this.red = red;
    this.green = green;
    this.blue = blue;
  }

  public Color()
  {
    this(0.0);
  }

  public Color(double k)
  // construct a gray
  {
    this(k,k,k);
  }

  public double red()
  {
    return red;
  }

  public double green()
  {
    return green;
  }

  public double blue()
  {
    return blue;
  }

  public boolean equals(Color that)
  {
    return this.red() == that.red() &&
    this.green() == that.green() &&
    this.blue() == that.blue();
  }

  public String toString()
  // construct a string "representation" of this
  {
    return "("+red()+","+green()+","+blue()+")";
  }

  public static void main(String[] args)
  {
    Color c = new Color(1.0,0.0,0.0);
    Color d = new Color(1.0,1.0,0.0);
    System.out.println(c.equals(d));
    System.out.println(c);
    System.out.println(d);
  }
}
