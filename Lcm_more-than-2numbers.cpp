#include <iostream>
using namespace std;

// Function to calculate the GCD (Greatest Common Divisor)
int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

// Function to calculate the LCM (Least Common Multiple)
int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

// Function to calculate the LCM of an array of numbers
int lcmMultiple(int arr[], int n) {
    int result = arr[0];
    for (int i = 1; i < n; i++) {
        result = lcm(result, arr[i]);
    }
    return result;
}

int main() {
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    int arr[n];
    std::cout << "Enter the elements: ";
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    int result = lcmMultiple(arr, n);
    std::cout << "The LCM of the numbers is: " << result << std::endl;

    return 0;
}

