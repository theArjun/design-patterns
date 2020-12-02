package singleton;

/* OS as singleton class. */

class OS {
    /* 1. Create a static object. */
    static OS obj = new OS();
    int value = 10;


    /* 2. The user shouldn't be able to 
    create instance through constructor. */
    private OS() {
    }

    /* 3. Static method to return object 
    which also return static object. */
    public static OS getInstance() {
        return obj;
    }

    /* 4. (Optional) Create a method to 
    alter the value(value) so that we can
    observer the instance being shared
    among every objects.*/
    public void setValue(int value){
        this.value = value;
    }
}