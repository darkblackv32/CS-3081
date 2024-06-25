#include <pybind11/pybind11.h>
#include <map>
#include <string>
#include <vector>
#include <iostream>

class SimpleClass{
public:
    SimpleClass(int initial_value) : value(initial_value) {}
    void setValue(int new_value) {value = new_value;}
    int getValue() const {return value;}
    std::string setMapValue(std::string const &k, std::string const& v){
        example_map[k] = v;
        return v;
    }

    std::string showMapValue(){
        std::string ret = "";
        for(auto it = example_map.begin(); it!= example_map.end(); it++){
            ret += (it->first + " " + it->second + "\n");
        }
        return ret;
    }

private:
    int value;
    std::vector<int> numbers;
    std::map<std::string, std::string> example_map;

};

namespace py = pybind11;

PYBIND11_MODULE(example, m) {
    py::class_<SimpleClass>(m, "SimpleClass")
    .def(py::init<int>())
    .def("set_value", &SimpleClass::setValue)
    .def("get_value", &SimpleClass::getValue)
    .def("setMapValue", &SimpleClass::setMapValue)
    .def("showMapValue", &SimpleClass::showMapValue);
}