#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    int value;
    struct node *left;
    struct node *right;
    int height;
} node;

int height(struct node *root)
{
    if (root == NULL)
        return 0;
    return root->height;
}

int max(int left, int right)
{
    return (left > right) ? left : right;
}

int getBalance(struct node *root)
{
    if (root == NULL)
        return 0;
    return height(root->left) - height(root->right);
}

node *push(node *root, int value)
{
    node *new = malloc(sizeof(node));
    if (new == NULL)
    {
        printf("Error: unable to allocate memory\n");
        return NULL;
    }

    if (root == NULL)
    {
        new->value = value;
        new->left = NULL;
        new->right = NULL;
        new->height = 1;
        return new;
    }

    if (value < root->value)
    {
        root->left = push(root->left, value);
    }
    else if (value > root->value)
    {
        root->right = push(root->right, value);
    }


    root->height = 1 + max(height(root->left), height(root->right));

    return root;

}

int main(int argc, char **argv)
{
    node *root = NULL;
    // printf("%d\n", argc);
    if (argc < 2)
    {
        printf("Error: not enough arguments\n");
        return 1;
    }
    int count = atoi(argv[1]);

    // create a binary tree of 10 elements
    for (int i = 0; i < count; i++)
    {
        root = push(root, i);
    }

    if (root != NULL)
    {
        printf("%d\n", root->value);
        printf("%d\n", getBalance(root));

    }
    return 0;


}