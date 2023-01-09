#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size, alloc;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
