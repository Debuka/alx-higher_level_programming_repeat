#include "lists.h"

/**
 * dlistint_len - returns all the
 * elements of a double linked list.
 *
 * @h: head of the list.
 * Return: num of the nodes.
 */

size_t dlistint_len(const dlistint_t *h)
{
	int idx;
	idx = 0;

	if (h == NULL)
		return (idx);
	while (h->prev != NULL)
		h = h->prev;
	while (h != NULL)
	{
		idx++;
		h = h->next;
	}
	return (idx);
}
