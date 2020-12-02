package factory;

/* Driver code for Factory design pattern. */

import java.util.Scanner;

class FactoryDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter operating system : ");
        String osType = sc.next();
        
        OS obj = OSFactory.getInstance(osType);
        if(obj != null){
            obj.spec();
        } else {
            System.out.println("Can't create object of given type.");
        }
        sc.close();
    }
}