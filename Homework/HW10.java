public class HW10 {

  public static void main(String args[]){

    boolean prime = true;
    int n = 6;
    for (int i = 2; i < n; i++) {
      if (n % i == 0) {
        prime = false;
      }
    }
    if (n == 1) {
      prime = false;
    }
    System.out.println(prime);
  }
}
