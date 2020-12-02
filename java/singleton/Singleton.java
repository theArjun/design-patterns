package singleton;

/* Class to demonstrate singleton behaviour of OS class. */

public class Singleton {
    public static void main(String[] args) {
        OS obj1 = OS.getInstance();
        OS obj2 = OS.getInstance();

        System.out.println(obj1.value);
        System.out.println(obj2.value);

        /* Changing the value property of obj1 object
        will also change the value property of obj2
        object. It happens because the instance is shared
        between every objects.
         */
        obj1.setValue(20);

        System.out.println(obj1.value);
        System.out.println(obj2.value);
    }
}
