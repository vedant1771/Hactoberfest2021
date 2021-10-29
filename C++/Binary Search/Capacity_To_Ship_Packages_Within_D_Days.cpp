class Solution {
public:



   //this ques is similar to minium number of maximum pages problem of gfg




    bool isFeasible(vector<int> weights, int days, int possible_ans)
    {

        int k = 1; //denoting days 
        int sum=0;

        for(int i=0;i<weights.size();i++)
        {
            if(sum+weights[i] > possible_ans)
            {
                sum = weights[i];
                k++;
            }

            else
                sum+=weights[i];


        }

        return (k<=days);


    }


    int shipWithinDays(vector<int>& weights, int days) {

        int sum=0, maximum = weights[0];
        int res=-1;

        for(int i=0;i<weights.size();i++)
        {
            sum+=weights[i];
            maximum = max(maximum,weights[i]);
        }

        int l = maximum;  //defining range for Binary Search
        int h = sum;

        int mid;

        while(l<=h)
        {

            mid = (l+h)/2;

            if(isFeasible(weights,days,mid))
            {
               res = mid;
                h=mid-1;
            }

            else
                l=mid+1;
        }

        return res;

    }
};
