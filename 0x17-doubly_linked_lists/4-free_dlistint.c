#include "lists.h"

/**
 *  free_dlistint - Function that frees a list.
 *
 *  @head: the head of the linked list.
 *  Return: nothing.
 */

void free_dlistint(dlistint_t *head)
{
	 dlistint_t *buff;

	 if (head != NULL)
		 while (head->prev != NULL)
			 head = head->prev;
	 while((buff = head) != NULL)
	 {
		 head = head->next;
		 free(buff);
	 }
}
