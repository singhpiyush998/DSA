#include <stdio.h>
#include <stdbool.h>
#define MAX_SIZE 1000

int stack[MAX_SIZE];
int top = -1;

bool isEmpty() {
    return top == -1;
}

void push(int x) {
    stack[++top] = x;
}

int pop() {
    if (isEmpty()) printf("Error: Stack is empty.\n");
    else top--;
    return stack[top + 1];
}

int peek() {
    if (isEmpty()) {
        printf("Error: Stack is empty.");
        return -12741;
    }
    return stack[top];
}

void display() {
    if (isEmpty()) printf("Error: Stack is empty\n");
    else {
        printf("Stack contents: ");
        for (int i = 0; i <= top; i++)
            printf("%d ", stack[i]);
        printf("\n");
    }
}

int main(void) {
    push(2);display();
    push(5);display();
    push(10);display();
    pop();display();
    push(12);display();
    return 0;
}
