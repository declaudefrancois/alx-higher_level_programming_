#include "Python.h"

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - prints basic info about
 * a python list.
 *
 * @p: A pointer to a generic PyObject.
 */
void print_python_list(PyObject *p)
{
	PyListObject *plo;
	int i;
	ssize_t size;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	plo = (PyListObject *)p;
	size = plo->ob_base.ob_size;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", plo->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, plo->ob_item[i]->ob_type->tp_name);
		if (strcmp(plo->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(plo->ob_item[i]);
		else if (strcmp(plo->ob_item[i]->ob_type->tp_name, "float") == 0)
			print_python_float(plo->ob_item[i]);
	}
}

/**
 * print_python_bytes -  print some basic info about
 * a Python bytes object.
 *
 * @p: A pointer to a generic PyObject.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *pbo;
	Py_ssize_t size;
	int max_bytes;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	pbo = (PyBytesObject *) p;
	size = pbo->ob_base.ob_size;
	max_bytes = size >= 10 ? 10 : size + 1;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", pbo->ob_sval);
	printf("  first %d bytes:", max_bytes);
	for (int i = 0; i < max_bytes; i++)
		printf(" %02x", pbo->ob_sval[i] & 0xff);

	printf("\n");
}

/**
 * print_python_float -  print some basic info about
 * a Python float object.
 *
 * @p: A pointer to a generic PyObject.
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *pfo;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	pfo = (PyFloatObject *) p;
	if ((int) pfo->ob_fval == pfo->ob_fval)
		printf("  value: %d.0\n", (int) pfo->ob_fval);
	else
		printf("  value: %1.16lG\n", pfo->ob_fval);
}
