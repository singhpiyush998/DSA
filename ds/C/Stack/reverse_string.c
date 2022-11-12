#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node Node;
struct Node {
    char data;
    Node* next;
};

Node* top = NULL;

// O(1)
bool isEmpty() {
    return top == NULL;
}

// O(1)
void push(char x) {
    Node* newNode = malloc(sizeof(Node));
    newNode->data = x;
    newNode->next = top;
    top = newNode;
}

// O(1)
char pop() {
    Node* tmp = top;
    top = top->next;
    char data = tmp->data;
    free(tmp);
    return data;
}

int main(void) {
    char s[] = "Hello";
    int i = 0;
    while (s[i] != '\0') {
        push(s[i]);
        i++;
    }
    
    printf("%s\n", s);

    int j = 0;
    while (s[j] != '\0') {
        s[j] = pop();
        j++;
    }

    printf("%s\n", s);

    return 0;
}
