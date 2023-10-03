#include "lists.h"

/**
 * check_cycle - Function that checks for a circle in a linked list.
 * @list: list to be checked.
 *
 * Return: 1 if circle is preent, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *a_pace = list;
	listint_t *two_pace = list;

	if (!list)
		return (0);

	while (a_pace && two_pace && two_pace->next)
	{
		a_pace = a_pace->next;
		two_pace = two_pace->next->next;
		if (a_pace == two_pace)
			return (1);
	}

	return (0);
}
