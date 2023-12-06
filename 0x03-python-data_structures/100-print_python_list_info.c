#include <Python.h>

/**
 * print_python_list_info - function that prints some basic
 * info about Python lists
 * @p: the python object list
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size_, alloc_, idx_;
	PyListObject *listed;

	size_ = PyList_Size(p);
	alloc_ = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size_);
	printf("[*] Allocated = %ld\n", alloc_);

	for (idx_ = 0; idx_ < size_; idx_++)
	{
		listed = (PyListObject *)p;
		printf("Element %ld: %s\n",
				idx_, Py_TYPE(list->ob_item[idx])->tp_name);
	}
}
