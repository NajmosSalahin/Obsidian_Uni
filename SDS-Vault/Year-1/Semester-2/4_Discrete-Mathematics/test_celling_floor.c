#include <stdio.h>
#include<math.h>

int main() {
    double x;
    int floor_val, ceiling_val;

    // Step 2: Get the number
    printf("Enter a decimal number: ");
    if (scanf("%lf", &x) != 1)
        {
        printf("Invalid input.\n");
        return 1;
    }

    // Step 3: Find the Floor value (Round Down)
    int temp_floor = (int)x; // Drop the decimal part of x

    if (x == temp_floor)
        {
        floor_val = temp_floor; // If x has no decimals
       }
    else if (x < 0)
        {
        floor_val = temp_floor - 1; // If x is negative
    }
    else
        {
        floor_val = temp_floor; // Otherwise, for positive numbers
    }

    // Step 4: Find the Ceiling value (Round Up)
    int temp_ceil = (int)x; // Drop the decimal part of x

    if (x == temp_ceil) {
        ceiling_val = temp_ceil; // If x has no decimals
    } else if (x > 0) {
        ceiling_val = temp_ceil + 1; // If x is positive
    } else {
        ceiling_val = temp_ceil; // Otherwise, for negative numbers
    }

    // Step 5: Print the answers
    printf("\n--- Results ---\n");
    printf("Original Value: %.3f\n", x);
    printf("Floor Value:    %d\n", floor_val);
    printf("Ceiling Value:  %d\n", ceiling_val);

    return 0; // Step 6: End
}
