class OSFactory {
    public static OS getInstance(String type){
        if (type.equals("ios")){
            return new IOS();
        } else if (type.equals("android")){
            return new Android();
        } else if (type.equals("windows")){
            return new Windows();
        } else {
            return null;
        }
    }
}