#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node Node;
struct Node {
    int data;
    Node* next;
};

Node* head = NULL; // To store the address of head node not the head node itself

// O(n)
int length() {
    Node* tmp = head;
    int i;
    for (i = 0; tmp != NULL; i++) tmp = tmp->next;
    return i;
}

// O(n)
Node* getNode(int index) {
    if (index < 0 || index > length() - 1) return NULL;
    Node* current = head;
    for (int i = 0; i < index; i++) current = current->next;
    return current;
}

// O(1)
void addToHead(int data) {
    Node* tmp = malloc(sizeof(Node));
    tmp->data = data;
    tmp->next = head;
    head = tmp;
}

// O(n), We can make it O(1) by always storing a pointer to tail.
void addToTail(int data) {
    Node* tmp = malloc(sizeof(Node));
    tmp->data = data;
    tmp->next = NULL;
    if (head == NULL) head = tmp;
    else {
        Node* tail = head;
        while (tail->next != NULL) tail = tail->next;
        tail->next = tmp;
    }
}

// O(n)
void addAtIndex(int data, int n) {
    if (n < 0 || n > length()) printf("\nEnter a valid index.\n");
    else if (head == NULL) {
        if (n == 0) addToHead(data);
        else printf("\nList is empty so index must be 0.\n");
    }
    else {
        Node* prev = head;
        for (int i = 0; i < n - 1; i++) prev = prev->next;
        Node* newNode = malloc(sizeof(Node));
        newNode->data = data;
        newNode->next = prev->next;
        prev->next = newNode;
    }
}

// O(n)
void deleteAtIndex(int n) {
    if (head == NULL) printf("\nList is empty!\n");
    else if (n < 0 || n > length() - 1) printf("\nEnter a valid index\n");
    else if (n == 0) {
        Node* tmp = head;
        head = head->next;
        free(tmp);
    }
    else {
        Node* prev = head;
        for (int i = 0; i < n - 1; i++) prev = prev->next;
        Node* current = prev->next;
        prev->next = current->next;
        free(current);
    }
}

// O(1)
void deleteNextNode(Node* prev) {
    if (prev == NULL) printf("Can't delete there!\n");
    else {
        Node* tmp = prev->next;
        prev->next = tmp->next;
        free(tmp);
    }
}

// O(1)
void addAfterNode(Node* prev, int data) {
    if (prev == NULL) printf("Cant' add there!\n");
    else {
        Node* tmp = malloc(sizeof(data));
        tmp->data = data;
        tmp->next = prev->next;
        prev->next = tmp;
    }
}

// O(n)
void print() {
    if (head == NULL) printf("List is empty\n");
    else {
        Node* current = head;
        printf("\n");
        while (current != NULL) {
            printf("%d ", current->data);
            current = current->next;
        }
        printf("\n");
    }
}

int main(void) {
    bool is_running = true;
    int op;
    while(is_running) {
        char* ops = "1. Insert at start.\n2. Insert at End.\n3. Insert at Index.\n"
                    "4. Delete at Index.\n5. Print the list.\n6. Exit.\n";
        printf("%sSelect the option: ", ops);
        scanf("%d", &op);
        int data, index;
        switch (op) {
            case 1:
                printf("Enter the integer: ");
                scanf("%d", &data);
                addToHead(data);
                break;
            case 2:
                printf("Enter the integer: ");
                scanf("%d", &data);
                addToTail(data);
                break;
            case 3:
                printf("Enter the index: ");
                scanf("%d", &index);
                printf("Enter the interger: ");
                scanf("%d", &data);
                // addAtIndex(data, index);
                addAfterNode(getNode(index - 1), data);
                break;
            case 4:
                printf("Enter the index: ");
                scanf("%d", &index);
                deleteAtIndex(index);
                // deleteNextNode(getNode(index - 1));
                break;
            case 5:
                print();
                break;
            case 6:
                is_running = false;
                break;
            default:
                printf("\nPlease select a correct option.\n");
        }
    }
    return 0;
}


