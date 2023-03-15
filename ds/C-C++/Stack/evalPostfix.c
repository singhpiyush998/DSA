#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node Node;
struct Node {
    int data;
    Node* next;
};

Node* top = NULL;

// O(1)
bool isEmpty() {
    return top == NULL;
}

// O(1)
void push(int x) {
    Node* newNode = malloc(sizeof(Node));
    newNode->data = x;
    newNode->next = top;
    top = newNode;
}

// O(1)
int pop() {
    if (isEmpty()) return '\0';
    int data = top->data;
    top = top->next;
    return data;
}

int perform(int op1, int op2, char opr) {
    switch (opr) {
        case '+':
            return op1 + op2;
            break;
        case '-':
            return op1 - op2;
            break;
        case '*':
            return op1 * op2;
            break;
        case '/':
            return op1 / op2;
            break;
        default:
            return '0';
    }
}

// Assume that operands are 1 digit numbers and postifix expression is valid.
int evalPostfix(char* exp) {
    int i = 0;
    char c = exp[i];
    while (c) {
        if (c >= '0' && c <= '9') push(c - '0');
        else if(c == '+' || c == '-' || c == '*' || c == '/') {
            int o2 = pop();
            int o1 = pop();
            int eval = perform(o1, o2, c);
            push(eval);
        }
        c = exp[++i];
    }
    return top->data;
}

int main(void) {
    char* exp = "762+*42/-";
    printf("The result is: %d\n", evalPostfix(exp));
    return 0;
}
