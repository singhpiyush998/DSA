#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node Node;
struct Node {
    char data;
    Node* next;
};

Node* top = NULL;

void push(char data) {
    Node* newNode = malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = top;
    top = newNode;
}

void pop() {
    if (top == NULL) return;
    Node* tmp = top;
    top = top->next;
    free(tmp);
}

char peek() {
    if (top) return top->data;
    return '\0';
}

bool checkBalancedParethesis(char* exp) {
    int i = 0;
    char c = exp[i];
    while (c) {
        if (c == '(' || c == '{' || c == '[') push(c);
        else if (c == ')' || c == '}' || c == ']') {
            char last = peek();
            if (last && (
                (c == ')' && last == '(') ||
                (c == '}' && last == '{') ||
                (c == ']' && last == '[')
                )
            ) pop();
            else return false;
        }
        c = exp[++i];
    }
    return top == NULL;
}

int main(void) {
    char* str = "[(a * 2) + {(a + b) * (A + B)}]";
    bool res = checkBalancedParethesis(str);
    if (res) printf("The equation has balanced parenthesis.\n");
    else printf("The equation does't have balance parenthesis.\n");
    return 0;
}
