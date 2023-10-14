#include "lists.h"

/**
 * get_dnodeint_at_index - Function that returns
 * the nth node of a dlistint_t linked list.
 *
 * @head: head os the list.
 * @index: index of nth node.
 * Return: the nth node.
 */

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int k = 0;

	if (head == NULL)
		return (NULL);
	while (head->prev != NULL)
		head = head->prev;
	while (head != NULL)
	{
		if (k != index)
			break;
		head = head->next;
		k++;
	}
}
