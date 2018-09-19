public class Helicopter {

    private float maximumLiftingWeight;
    private String name;
    private float maximumHeight;

    public Helicopter(float maximumLiftingWeight, String name, float maximumHeight) {
        this.maximumLiftingWeight = maximumLiftingWeight;
        this.name = name;
        this.maximumHeight = maximumHeight;
    }

    public float getMaximumLiftingWeight() {
        return maximumLiftingWeight;
    }

    public void setMaximumLiftingWeight(float maximumLiftingWeight) {
        this.maximumLiftingWeight = maximumLiftingWeight;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public float getMaximumHeight() {
        return maximumHeight;
    }

    public void setMaximumHeight(float maximumHeight) {
        this.maximumHeight = maximumHeight;
    }
}
