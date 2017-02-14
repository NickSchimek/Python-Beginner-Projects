/** MultiplicationChart - Generates a multiplication table.
 *
 * @author Miafro
 */
public class MultiplicationChart {
    
    /** createMultiplicationChart - creates a multiplication chart from 1 to 
     *  range.
     * 
     * @param range - The range of the chart.
     */
    public static void createMultiplicationChart(int range) {
        int num;       

        range += 1;       
        System.out.println("\n");

        
        for (int n = 1; n < range; n++) {
            num = n;
            for (int x = 1; x < range; x++){
                System.out.printf(" %8d", num);
                num += n;
            }
            System.out.println("\n");
        }
    }
}
