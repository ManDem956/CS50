#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    char value;
    struct node *prev;
} stack;

void push(stack **head, char value)
{
    // Check if head is null
    if (head == NULL)
    {
        printf("Error: head is null\n");
        return;
    }

    // Allocate memory for new node
    stack *new = malloc(sizeof(stack));
    if (new == NULL)
    {
        printf("Error: unable to allocate memory\n");
        return;
    }

    // Set the value and prev pointer of new node
    new->value = value;
    new->prev = *head;

    // Update the head pointer
    *head = new;
}

stack *pop(stack **head)
{

    if (head == NULL)
    {
        printf("Error: head is null\n");
        return NULL;
    }

    stack *current = *head;

    *head = (*head)->prev;

    return current;
}

void print_list(stack **head)
{
    stack *current = *head;

    while (current != NULL)
    {
        printf("%d\n", current->value);
        current = current->prev;
    }
}

int main(int argc, char **argv)
{
    stack *head = NULL;
    // printf("%d\n", argc);
    if (argc < 2)
    {
        printf("Error: not enough arguments\n");
        return 1;
    }
    int count = atoi(argv[1]);

    // Create a stack of 10 elements
    for (int i = 0; i < count; i++)
    {
        push(&head, i);
    }

    if (head != NULL)
    {
        print_list(&head);
    }
    if (head != NULL)
    {
        print_list(&head);
    }

    while (head != NULL)
    {
        stack *current = pop(&head);
        printf("%d\n", current->value);
        free(current);
    }

    return 0;
}
