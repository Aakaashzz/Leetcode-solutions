class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
		var max = 0
		val hashSet = LinkedHashSet<Char>()
		
		for(c in s) {
			while(hashSet.contains(c)) {
				if(max < hashSet.size) {
					max = hashSet.size
				}
				hashSet.remove(hashSet.first())
			}
            hashSet.add(c)
		}
		
		if(max < hashSet.size) {
			max = hashSet.size
		}
		
		return max
    }
}