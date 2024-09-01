#include <pybind11/pybind11.h>

namespace py = pybind11;

int mul(int a, int b) {
    return a * b;
}

PYBIND11_MODULE(cpp_example, m) {
    m.doc() = "pybind11 c++ example";
    m.def("mul", &mul, "Multiply 2 integers");
}

