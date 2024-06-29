#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    char value;
    struct node *next;
} queue;

void enqueue(queue **head, char value)
{
    // Allocate memory for new node
    queue *new = malloc(sizeof(queue));
    if (new == NULL)
    {
        printf("Error: unable to allocate memory\n");
        return;
    }

    // Set the value and next pointer of new node
    new->value = value;
    new->next = NULL;

    // If the queue is empty, update head
    if (*head == NULL)
    {
        *head = new;
    }
    else
    {
        // Find the last node in the queue
        queue *last = *head;
        while (last->next != NULL)
        {
            last = last->next;
        }

        // Add new node to the end of the queue
        last->next = new;
    }
}

void dequeue(queue **head)
{
    if (head == NULL || *head == NULL)
    {
        return;
    }

    queue *current = *head;
    queue *previous = NULL;

    while (current->next != NULL)
    {
        previous = current;
        current = current->next;
    }

    if (previous != NULL)
    {
        previous->next = NULL;
        free(current);
    }
    else
    {
        *head = NULL;
        free(current);
    }
}

void print_list(queue **head)
{
    queue *current = *head;

    while (current != NULL)
    {
        printf("%d ", current->value);
        current = current->next;
    }
    printf("\n");
}

int main(int argc, char **argv)
{
    queue *head = NULL;
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
        enqueue(&head, i);
    }

    if (head != NULL)
    {
        print_list(&head);
    }
    // if (head != NULL)
    // {
    //     print_list(&head);
    // }

    while ((head != NULL) && (head->next != NULL))
    {
        dequeue(&head);
        print_list(&head);
    }
    free(head);

    return 0;
}
