class Solution {
public:
    
    int value(char roman){
    switch(roman){
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
    }
    return -1;
}
int romanToInt(string s) {
    int i;
    int ans=0;
    int n = s.length()-1;
    for(i=n;i>=0;i--){
        if(value(s[i])>= value(s[i+1])){
            ans = ans + value(s[i]);
        }
        else
        {
            ans = ans - value(s[i]);
        }

    }return ans;
}
        
};
