#include <iostream>
#include <queue>
using namespace std;

typedef struct Node {
    Node* left;
    Node* right;
    int data;
} Node ;

void BFS(Node* root) {
    if (root == NULL) return;

    queue<Node*> q;
    q.push(root);

    while (!q.empty()) {
        Node* curr = q.front();
        cout << curr->data << " ";
        if (curr->left != NULL) q.push(curr->left);
        if(curr->right != NULL) q.push(curr->right);
        q.pop();
    }
}

int main (void)
{
    Node* root = new Node();
    root->data = 5;
    root->left = new Node();
    root->right = new Node();

    root->left->data = 7;
    root->right->data = 6;

    BFS(root);
    free(root);
    return 0;
}
