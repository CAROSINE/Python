#include <stdio.h>

int main() {
    int emp_number, worked_hours;
    float rate_per_hour, salary;

    // Reading input values
    scanf("%d", &emp_number);
    scanf("%d", &worked_hours);
    scanf("%f", &rate_per_hour);

    // Calculating salary
    salary = worked_hours * rate_per_hour;

    // Printing output with proper formatting
    printf("NUMBER = %d\n", emp_number);
    printf("SALARY = U$ %.2f\n", salary);

    return 0;
}

