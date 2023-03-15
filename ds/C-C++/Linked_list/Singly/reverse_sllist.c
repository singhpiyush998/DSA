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

void reverse() {
    Node* prev = NULL;
    Node* current = list;
    while (current != NULL) {
        Node* next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    list = prev;
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

int main(void) {
    insert_at_end(5);
    insert_at_end(6);
    insert_at_end(7);
    printf("Linked list: ");
    print();
    reverse();
    printf("Linked list after reversing: ");
    print();
    return 0;
}
