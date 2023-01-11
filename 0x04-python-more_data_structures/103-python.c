#include <python3.8/Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;
	Py_ssize_t i;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", var->ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < var->ob_size; i++)
	{
		printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
		if (PyBytes_Check(list->ob_item[i]))
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: pointer to PyObject
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	PyVarObject *var = (PyVarObject *)p;
	Py_ssize_t i, size;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = var->ob_size;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (size < 10)
		printf("  first %ld bytes:", size + 1);
	else
		printf("  first 10 bytes:");

	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", bytes->ob_sval[i]);
	printf("\n");
}
