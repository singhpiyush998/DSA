#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node Node;
struct Node {
    int data;
    Node* next;
};

Node* front = NULL;
Node* rear = NULL;

bool isEmpty() {
    return (front == NULL && rear == NULL);
}

int Front() {
    if (isEmpty()) return -1;
    return front->data;
}

void enqueue(int x) {
    Node* newNode = malloc(sizeof(Node));
    newNode->data = x;
    newNode->next = NULL;

    if (isEmpty()) front = rear = newNode;
    else {
        rear->next = newNode;
        rear = newNode;
    }
}

void dequeue() {
    Node* tmp = front;
    if (isEmpty()) return;
    else if (front == rear) front = rear = NULL;
    else front = front->next;
    free(tmp);
}

void print() {
    if (isEmpty()) printf("The list is empty.\n");
    else {
        Node* tmp = front;
        while (tmp != NULL) {
            printf("%d ", tmp->data);
            tmp = tmp->next;
        }
        printf("\n");
    }
}

int main(void) {
    enqueue(5);print();
    enqueue(6);print();
    enqueue(7);print();
    dequeue(); print();
    enqueue(8);print();
    dequeue(); print();
    return 0;
}
