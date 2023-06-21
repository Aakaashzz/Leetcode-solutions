public class Solution {
    public bool IsValid(string s) {
        Dictionary<char, char> bracketsMap = new Dictionary<char, char>{
            {'{',  '}'},
            {'(',  ')'},
            {'[',  ']'},
        };
        Stack<char> openBrackets = new Stack<char>();
        
        foreach (char bracket in s) {
            if (bracketsMap.ContainsKey(bracket)) {
                openBrackets.Push(bracket);
            } else {
                 if (openBrackets.Count == 0) {
                    return false;
                }
                if (bracketsMap[openBrackets.Pop()] == bracket) {
                    continue;
                };
                return false;
            }
        }
        return openBrackets.Count == 0;
    }
}