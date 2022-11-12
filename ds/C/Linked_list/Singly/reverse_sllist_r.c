#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node Node;
struct Node {
    int data;
    Node* next;
};

Node* list = NULL; // To store the address of head node not the head node itself

void insert_at_end(int data) {
    Node* tmp = malloc(sizeof(Node));
    tmp->data = data;
    tmp->next = NULL;
    if (list == NULL) {
        list = tmp;
    } else {
        Node* last = list;
        while (last->next != NULL) {
            last = last->next;
        }
        last->next = tmp;
    }
}

void print() {
    if (list == NULL) {
        printf("The list is empty\n");
    } else {
        Node* current = list;
        printf("\n");
        while (current != NULL) {
            printf("%d ", current->data);
            current = current->next;
        }
        printf("\n");
    }
}

void reverse(Node* current, Node* prev) {
    if (current->next == NULL) list = current;
    else reverse(current->next, current);
    current->next = prev;
}

int main(void) {
    insert_at_end(5);
    insert_at_end(6);
    insert_at_end(7);
    printf("Linked list: ");
    print();
    reverse(list, NULL);
    printf("Linked list after reversing: ");
    print();
    return 0;
}
