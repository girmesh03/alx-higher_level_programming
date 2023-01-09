#include "lists.h"

void reverse(listint_t **head_of_second);
int compare(listint_t *head_of_first, listint_t *head_of_second);

/**
 * reverse_listint - reverses a listint_t linked list
 * @head: double pointer to head of list
 * Return: pointer to first node of reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	if (!head || !*head)
		return (NULL);

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}

/**
 * reverse - reverses a listint_t linked list
 * @head_of_second: double pointer to head of list
 * Return: pointer to first node of reversed list
 */

void reverse(listint_t **head_of_second)
{
	listint_t *prev = NULL;
	listint_t *current = *head_of_second;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head_of_second = prev;
}

/**
 * compare - compares two lists
 * @head_of_first: pointer to head of first list
 * @head_of_second: pointer to head of second list
 * Return: 1 if equal, 0 if not
 */

int compare(listint_t *head_of_first, listint_t *head_of_second)
{
	listint_t *temp1 = head_of_first;
	listint_t *temp2 = head_of_second;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}
	if (temp1 == NULL && temp2 == NULL)
		return (1);
	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head;
	listint_t *second_half, *prev_of_slow_ptr = *head;
	listint_t *midnode = NULL;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			prev_of_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		if (fast_ptr != NULL)
		{
			midnode = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		second_half = slow_ptr;
		prev_of_slow_ptr->next = NULL;
		reverse(&second_half);
		res = compare(*head, second_half);
		reverse(&second_half);
		if (midnode != NULL)
		{
			prev_of_slow_ptr->next = midnode;
			midnode->next = second_half;
		}
		else
			prev_of_slow_ptr->next = second_half;
	}
	return (res);
}
