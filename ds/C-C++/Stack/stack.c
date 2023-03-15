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
    if (isEmpty()) return -1;
    int data = top->data;
    top = top->next;
    return data;
}

// O(1)
int peek() {
    if (isEmpty()) return -1;
    return top->data;
}

// O(n)
void display() {
    if (isEmpty()) printf("Error: Stack is empty.");
    else {
        printf("Stack contents: ");
        Node* tmp = top;
        while (tmp != NULL) {
            printf("%d ", tmp->data);
            tmp = tmp->next;
        }
        printf("\n");
    }
}

int main(void) {
    push(5);  display();
    push(7);  display();
    push(9);  display();
    pop();    display();
    push(11); display();
    return 0;
}
