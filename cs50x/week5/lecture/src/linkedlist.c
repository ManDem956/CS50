#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct node
{
    int value;
    struct node *next;
} node;

void push(node **head, int value)
{
    node *new = malloc(sizeof(node));
    if (new == NULL)
    {
        printf("Error: unable to allocate memory\n");
        return;
    }
    new->value = value;
    new->next = *head;
    *head = new;
}

void enqueue(node **head, int value)
{
    node *new = malloc(sizeof(node));
    if (new == NULL)
    {
        printf("Error: unable to allocate memory\n");
        return;
    }
    new->value = value;
    new->next = NULL;

    if (*head == NULL)
    {
        *head = new;
    }
    else if (new->value < (*head)->value)
    {
        new->next = *head;
        *head = new;
    }
    else
    {
        for (node *current = *head; current != NULL; current = current->next)
        {
            if (current->next == NULL)
            {
                current->next = new;
                break;
            }

            if (new->value < current->next->value)
            {
                new->next = current->next;
                current->next = new;
                break;
            }
        }
    }
}

int pop(node **head)
{
    int result = -1;

    if (head == NULL)
    {
        printf("Error: head is null\n");
        return result;
    }
    node *current = *head;

    result = current->value;
    *head = (*head)->next;

    free(current);
    return result;
}

int main(int argc, char **argv)
{
    srand(time(NULL));
    node *head = NULL;
    // printf("%d\n", argc);
    if (argc < 2)
    {
        printf("Error: not enough arguments\n");
        return 1;
    }
    int count = atoi(argv[1]);

    // create a linked list of 10 elements

    for (int i = 0; i < count; i++)
    {
        enqueue(&head, i);
    }

    for (int i = 0; i < count; i++)
    {
        push(&head, i);
    }

    while (head != NULL)
    {
        printf("%d ", pop(&head));
        // free(current);
        // current = current->next;
    }
    printf("\n");
}
