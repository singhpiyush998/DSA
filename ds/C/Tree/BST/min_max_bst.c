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

// int findMin(BstNode *root) {
//   if (root == NULL) {
//     printf("ERROR: The tree is empty.\n");
//     return -1;
//   }
//   while (root->left != NULL)
//     root = root->left;
//   return root->data;
// }

int findMin(BstNode *root) {
  if (root == NULL) {
    printf("ERROR: The tree is empty.\n");
    return -1;
  }
  if (root->left == NULL)
    return root->data;
  return findMin(root->left);
}

int findMax(BstNode *root) {
  if (root == NULL) {
    printf("ERROR: The tree is empty.\n");
    return -1;
  }
  if (root->right == NULL)
    return root->data;
  return findMax(root->right);
}
int main(void) {
  BstNode *root = NULL;
  root = insert(root, 15);
  root = insert(root, 10);
  root = insert(root, 20);
  root = insert(root, 20);
  root = insert(root, 25);
  root = insert(root, 8);
  root = insert(root, 12);

  printf("Minimum element in the BST is: %d\n", findMin(root));
  printf("Maximum element in the BST is: %d\n", findMax(root));

  return 0;
}
