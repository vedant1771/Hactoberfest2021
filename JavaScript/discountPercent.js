/**
 * This function calc the discount percent of 2 into parameters
 * @param price: ejm 450.00
 * @param salePrice: ejm 315.00
 * @returns {string|number}: result 35%
 */

const getPercentPrice = (price, salePrice)=>{
  if(price !== salePrice){
    return ((salePrice * 100 / price) - 100).toFixed(0);
  }else{
    return 0;
  }
}
