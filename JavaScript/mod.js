/* this is a modulo of a negative number 
    learn what it means here:
     https://torstencurdt.com/tech/posts/modulo-of-negative-numbers/
 */
function mod(a, b) {
  let c = a % b
    return (c < 0) ? c + b : c
}
