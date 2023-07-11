class Solution {
public:
    bool isNumber(string s) {
        int n = s.length();
        int i = 0;

        // Skip leading white space
        while (i < n && isspace(s[i])) {
            i++;
        }

        // Check optional sign
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            i++;
        }

        // Check digits before decimal point
        bool hasDigits = false;
        while (i < n && isdigit(s[i])) {
            i++;
            hasDigits = true;
        }

        // Check optional decimal point and digits after it
        if (i < n && s[i] == '.') {
            i++;
            while (i < n && isdigit(s[i])) {
                i++;
                hasDigits = true;
            }
        }

        // Check optional exponent part
        if (hasDigits && i < n && (s[i] == 'e' || s[i] == 'E')) {
            i++;

            // Check optional sign in exponent
            if (i < n && (s[i] == '+' || s[i] == '-')) {
                i++;
            }

            bool hasExponentDigits = false;
            while (i < n && isdigit(s[i])) {
                i++;
                hasExponentDigits = true;
            }

            // The exponent must have at least one digit
            if (!hasExponentDigits) {
                return false;
            }
        }

        // Check trailing white space
        while (i < n && isspace(s[i])) {
            i++;
        }

        // The number is valid if we consumed the entire string and found at least one digit
        return i == n && hasDigits;
    }
};