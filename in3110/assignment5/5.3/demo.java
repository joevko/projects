public class AddTwoNumbers {

   public static void main(String[] args) {
     //adding two number
      int num1 = 5, num2 = 15, sum;
      sum = num1 + num2;

      System.out.println("Sum of these numbers: "+sum);
   }
}

class ForLoopExample {

    public static void main(String[] args) {
         for (int i = 10; i > 1; i--){
              System.out.println("The value of i is: "+i);
         }
    }
}

class IfStatementExample {

  int timea = 20;

  if (timea < 18) {
    System.out.println("Good day.");
  } else {
    System.out.println("Good evening.");
  }
}



  int i = 0;
  do {
    System.out.println(i);
    i++;
  }
  while (i < 5);
