#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - The function that prints bytes info.
 *
 * @p: Python Obj.
 * Return: Nothing.
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, li;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		li = 10;
	else
		li = size + 1;

	printf("  first %ld bytes:", li);

	for (i = 0; i < li; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list - funct for Printing a list
 *
 * @p: Python Object
 * Return: Nothing.
 */
void print_python_list(PyObject *p)
{
	long int size, k;
	PyListObject *list;
	PyObject *j;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (k = 0; k < size; k++)
	{
		j = ((PyListObject *)p)->ob_item[k];
		printf("Element %ld: %s\n", k, ((j)->ob_type)->tp_name);
		if (PyBytes_Check(j))
			print_python_bytes(j);
	}

