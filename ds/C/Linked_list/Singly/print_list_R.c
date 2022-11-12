#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node Node;
struct Node {
    int data;
    Node* next;
};

Node* list = NULL; // To store the address of head node not the head node itself

void insert_at_start(int data) {
    Node* tmp = malloc(sizeof(Node));
    tmp->data = data;
    tmp->next = list;
    list = tmp;
}

void print_forward(Node* current) {
    if (current == NULL) printf("\n");
    else {
        printf("%d ", current->data);
        print_forward(current->next);
    }
}

void print_reverse(Node* current) {
    if (current == NULL) return;
    else {
        print_reverse(current->next);
        printf("%d ", current->data);
    }
}

int main(void) {
    insert_at_start(5);
    insert_at_start(4);
    insert_at_start(3);
    printf("Forward order:\n");
    print_forward(list);
    printf("Reverse order:\n");
    print_reverse(list);
    printf("\n");
    return 0;
}
