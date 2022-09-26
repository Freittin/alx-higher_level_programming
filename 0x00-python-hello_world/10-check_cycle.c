#include "lists.h"

/**
 * check_cycle - function that checks if a linked list has a cycle
 * @list: linked list to be checked
 * Return: 1 if has a cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp = list;
	listint_t *tmp2 = list;

	if (!list)
	{
		return (0);
	}
	while (tmp && tmp2 && tmp2->next)
	{
		tmp = tmp->next;
		tmp2 = tmp2->next->next;
		if (tmp == tmp2)
		{
			return (1);
		}
	}
	return (0);
}
