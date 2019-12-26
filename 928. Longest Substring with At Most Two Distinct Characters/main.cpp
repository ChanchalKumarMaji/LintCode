class Solution {
public:
    /**
     * @param s: a string
     * @return: the length of the longest substring T that contains at most 2 distinct characters
     */
    int lengthOfLongestSubstringTwoDistinct(string &s) {
        // Write your code here
        int count[256] = {0}; 
        int num = 0, i = 0, res = 0;
        for(int j=0; j<s.length(); j++){
            if(count[s[j]]++ == 0) num++;
            if(num > 2){
                while(--count[s[i++]] > 0);
                num--;
            }
            res = max(res,j-i+1);
        }
        
        return res;
    }
};
