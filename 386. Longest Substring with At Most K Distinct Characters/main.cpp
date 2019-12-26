class Solution {
public:
    /**
     * @param s: A string
     * @param k: An integer
     * @return: An integer
     */
    int lengthOfLongestSubstringKDistinct(string &s, int k) {
        // write your code here
        int count[256] = {0}; 
        int num = 0, i = 0, res = 0;
        for(int j=0; j<s.length(); j++){
            if(count[s[j]]++ == 0) num++;
            if(num > k){
                while(--count[s[i++]] > 0);
                num--;
            }
            res = max(res,j-i+1);
        }
        
        return res;
    }
};
