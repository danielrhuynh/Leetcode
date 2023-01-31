import scala.collection.mutable.HashMap

object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        var seen = new HashMap[Int, Int]()
        
        // For loop in scala where zipWithIndex is like enumerate and the arrow is a generator for the loop range
        for ((element, index) <- nums.zipWithIndex) {
            // Find required int
            // Check if required is in seen
            // If True return accessed index, and current index
            var required: Int = target-element
            if (seen.contains(required)) {
                // accessing from hashmaps returns a some() type which needs to be accessed again using get
                return Array(index, seen.get(required).get)
            }
            // If not found place element and index in hashMap in the form element: index
            seen.put(element, index)
        }
        // Return short hand
        Array(0,0)
    }
}