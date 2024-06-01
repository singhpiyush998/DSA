#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct BstNode BstNode;
struct BstNode {
  int data;
  BstNode *left;
  BstNode *right;
};

BstNode *getNewNode(int data) {
  BstNode *newNode = malloc(sizeof(BstNode));
  newNode->left = newNode->right = NULL;
  newNode->data = data;
  return newNode;
}

BstNode *insert(BstNode *root, int data) {
  if (root == NULL) {
    // Tree is empty
    root = getNewNode(data);
  } else if (data <= root->data) {
    root->left = insert(root->left, data);
  } else {
    root->right = insert(root->right, data);
  }
  return root;
}

bool search(BstNode *root, int data) {
  if (root == NULL)
    return false;
  if (root->data == data)
    return true;
  else if (data <= root->data)
    return search(root->left, data);
  else
    return search(root->right, data);
}

int main(void) {
  // address of the root not the root itself and setting tree as empty
  BstNode *root = NULL;
  root = insert(root, 15);
  root = insert(root, 10);
  root = insert(root, 20);
  root = insert(root, 20);
  root = insert(root, 25);
  root = insert(root, 8);
  root = insert(root, 12);

  int number;
  printf("Enter a number to be searched: ");
  scanf("%d", &number);
  if (search(root, number))
    printf("Found\n");
  else
    printf("Not found\n");
  return 0;
}
