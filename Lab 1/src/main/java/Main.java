import java.util.ArrayList;
import java.util.List;

public class Main {
    static int coc; //comparison operation counter
    static int eoc; //exchange operation counter

    public static void main(String[] args) {
        List<Helicopter> helicopters = new ArrayList<Helicopter>();
        helicopters.add(new Helicopter(1225, "Bell 429", 761));
        helicopters.add(new Helicopter(380, "Robinson R44", 650));
        helicopters.add(new Helicopter(1088, "Eurocopter EC 130", 616));
        helicopters.add(new Helicopter(675, "BELL 407", 1054));

        coc = 0;
        eoc = 0;
        long startTime = System.nanoTime();
        selectionSort(helicopters);
        long estimatedTime = System.nanoTime() - startTime;

        System.out.println("SELECTION SORT");
        System.out.println("Algorithm running time : " + estimatedTime + " (nano)");
        System.out.println("The number of comparison operations : " + coc);
        System.out.println("Number of exchange operations : " + eoc);
        System.out.println("Sort result :");
        for (Helicopter helicopter: helicopters) {
            System.out.println("MaximumHeight = "+helicopter.getMaximumHeight());
        }



        coc = 0;
        eoc = 0;
        startTime = System.nanoTime();
        List<Helicopter> helicopters1 = sort(helicopters);
        estimatedTime = System.nanoTime() - startTime;

        System.out.println("\nMERGE SORT");
        System.out.println("Algorithm running time : " + estimatedTime);
        System.out.println("The number of comparison operations : " + coc);
        System.out.println("Number of exchange operations : " + eoc);
        System.out.println("Sort result :");
        for (Helicopter helicopter: helicopters1) {
            System.out.println("MaximumLiftingWeight() = "+helicopter.getMaximumLiftingWeight());
        }
    }

    public static List<Helicopter> sort(List<Helicopter> arr) {
        coc++;
        if (arr.size() < 2) {
            return arr;
        }

        int m = arr.size() / 2;

        List<Helicopter> arr1 = new ArrayList<>();
        arr1.addAll(arr.subList(0, m));
        List<Helicopter> arr2 = new ArrayList<>();
        arr2.addAll(arr.subList(m, arr.size()));

        return merge(sort(arr1), sort(arr2));
    }

    public static List<Helicopter> merge(List<Helicopter> arr1, List<Helicopter> arr2) {
        int n = arr1.size() + arr2.size();
        List<Helicopter> arr = new ArrayList<>();
        int i1 = 0;
        int i2 = 0;
        for (int i = 0; i < n; i++) {
            coc++;
            if (i1 == arr1.size()) {
                coc++;
                arr.add(i, arr2.get(i2++));
            } else if (i2 == arr2.size()) {
                coc+=2; eoc++;
                arr.add(i,arr1.get(i1++));
            } else {
                coc+=2; coc=+3;
                if (arr1.get(i1).getMaximumLiftingWeight() > arr2.get(i2).getMaximumLiftingWeight()) {
                    eoc++;
                    arr.add(i,arr1.get(i1++));
                } else {
                    eoc++;
                    arr.add(i,arr2.get(i2++));
                }
            }
        }
        return arr;
    }

    public static void selectionSort(List<Helicopter> helicopterList) {
        for (int min = 0; min < helicopterList.size() - 1; min++) {
            int least = min;
            for (int j = min + 1; j < helicopterList.size(); j++) {
                coc++;
                if (helicopterList.get(j).getMaximumHeight() < helicopterList.get(least).getMaximumHeight()) {
                    least = j;
                }
            }

            eoc++;
            Helicopter tmpHelicopter = helicopterList.get(min);
            helicopterList.set(min, helicopterList.get(least));
            helicopterList.set(least, tmpHelicopter);
        }
    }
}
