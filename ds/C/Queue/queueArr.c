#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 10

int front = -1;
int rear = -1;
int data[MAX_SIZE];

bool isEmpty() {
    return (front == -1 && rear == -1);
}

void enqueue(int x) {
    if ((rear + 1) % MAX_SIZE == front) return;

    if (isEmpty()) front = rear = 0; 
    else rear = (rear + 1) % MAX_SIZE;
    data[rear] = x;
}

void dequeue() {
    if (isEmpty()) return;

    if(front == rear) front = rear = -1;
    else front = (front + 1) % MAX_SIZE;
}

int Front() {
    if (isEmpty()) return -1;
    return data[front];
}

void print() {
    int size = (rear - front + MAX_SIZE) % MAX_SIZE + 1;
    for (int i = 0; i < size; i++) {
        int index = (front + i) % MAX_SIZE;
        printf("%d ", data[index]);
    }
    printf("\n");
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
