#include "lists.h"

/**
 * insert_node - Function in c that inserts a number into sorted singly-linked list.
 * @head: pointer to the head of the list.
 * @number: The number that will be inserted.
 *
 * Return: On failure - NULL.
 * Or a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *curr_node = *head, *new_n;

        new_n = malloc(sizeof(listint_t));
        if (new_n == NULL)
                return (NULL);
        new_n->n = number;

        if (curr_node == NULL || curr_node->n >= number)
        {
                new_n->next = curr_node;
                *head = new_n;
                return (new_n);
        }

        while (curr_node && curr_node->next && curr_node->next->n < number)
                curr_node = curr_node->next;

        new_n->next = curr_node->next;
        curr_node->next = new_n;

        return (new_n);
}
