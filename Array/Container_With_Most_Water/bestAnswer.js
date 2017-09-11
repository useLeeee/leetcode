/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    max = 0;
    s = 0;
    e = height.length-1;
    while(e>s){
        max = Math.max(max,Math.min(height[s],height[e])*(e-s));
        if(height[s]>height[e]){
            e--;
        }else{
            s++;
        }
    }
    return max
};