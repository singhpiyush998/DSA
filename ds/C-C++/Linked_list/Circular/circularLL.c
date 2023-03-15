#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;
struct Node {
    int data;
    Node* next;
};

Node* tail = NULL; // pointer to tail node, not tail node itself

void add_front(int data) {
    Node* tmp = malloc(sizeof(Node));
    tmp->data = data;

    if (tail == NULL) {
        tail = tmp;
        tail->next = tail;
    }
    tmp->next = tail->next;
    tail->next = tmp;
}

void add_back(int data) {
    Node* tmp = malloc(sizeof(Node));
    tmp->data = data;
    tmp->next = tail->next;
    tail->next = tmp;
    tail = tmp;
}

void add_at(int data, int n) {
    Node* tmp = malloc(sizeof(Node));
    tmp->data = data;

    if (n == 0) add_front(data);
    else {
        Node* prev = tail->next;
        for (int i = 0; i < n - 1; i++) prev = prev->next;
        tmp->next = prev->next;
        prev->next = tmp;
    }
}

// Expect user to give valid index 
void delete_node_at(int n) {
    if (tail == NULL)
        printf("List is empty!\n");
    else if (n == 0) {
        if (tail->next == tail) {
            free(tail);
            tail = NULL;
        } else {
            Node* head = tail->next;
            tail->next = head->next;
            free(head);
        }
    } 
    else {
        Node* prev = tail->next;
        for (int i = 0; i < n - 1; i++) prev = prev->next;

        Node* tmp = prev->next;
        prev->next = tmp->next;
        if (tmp == tail) tail = prev;
        free(tmp);
    }
}

void display() {
    if (tail == NULL) printf("List is empty!\n");
    else {
        Node* tmp = tail;
        do {
            tmp = tmp->next;
            printf("%d ", tmp->data);
        } while(tmp != tail);
        printf("\n");
    }
}

int main(void) {
    add_front(5);
    add_front(4);
    add_front(3);
    add_back(7);
    add_at(6, 3);
    display();
    // Deleting some node
    delete_node_at(2);
    display();
    return 0;
}
