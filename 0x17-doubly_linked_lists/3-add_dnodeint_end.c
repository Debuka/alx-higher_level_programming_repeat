#include "lists"
/**
 * add_dnodeint_end - function that adds a new
 * node at end of a list.
 * @head: head.
 * @n: value odf the elements.
 * Return: pointer address of te new elements
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *nw;
	dlistint_t *h;

	nw = malloc(sizeof(dlistint_t));
	if (nw == NULL)
		return (NULL);
	nw->n = n;
	nw->next = (NULL);
	h = *header;
	
	if (h != NULL)
	{
		while (h->next != NULL)
			h = h->next;
		h->next = nw
	}
}
