#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int array[2048];
	int i = 0, j = 0;

	if (head == NULL || *head == NULL)
		return (1);
	while (current != NULL)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}
	i--;
	while (j < i)
	{
		if (array[j] != array[i])
			return (0);
		j++;
		i--;
	}
	return (1);
}
