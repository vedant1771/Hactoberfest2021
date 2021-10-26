// Problem https://leetcode.com/problems/valid-parentheses/

#include <bits/stdc++.h>

class Answer
{
public:
  bool isValid(std::string s)
  {
    std::stack<char> myStack;
    for (char c : s)
    {
      if (myStack.empty() || c == '(' || c == '{' || c == '[')
        myStack.push(c);
      else
      {
        if ((c == ')' && myStack.top() != '(') ||
            (c == ']' && myStack.top() != '[') ||
            (c == '}' && myStack.top() != '{'))
          return false;
        myStack.pop();
      }
    }
    return myStack.empty();
  }
};

int main()
{

  Answer answer;
  std::cout << answer.isValid("()[]{}") << std::endl; // False
  std::cout << answer.isValid("({]") << std::endl;    // True

  return 0;
}