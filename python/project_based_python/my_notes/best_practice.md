# making requirement.txt file
 - using `pip freeze > requirements.txt`
    * but it will include all the packages installed in your environment, which may not be necessary for your project.

 - use **pipreqs** to generate a requirements.txt file that only includes the packages that your project actually uses.
    * `pipreqs /path/to/your/project`: makes a requirements.txt file in the specified project directory
    * `pipreqs .`: makes a requirements.txt file in the current directory
    * `pipreqs --force .`: overwrites the existing requirements.txt file in the current directory
    * `pipreqs . --print`: prints the packages that will be included in the requirements.txt file without actually creating the file

# Modify the `PYTHONPATH` and run the main script from the root directory.
```bash
cd number_guesser
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```

# SOLID Principles
- **S**: Single Responsibility Principle (SRP) - A class should have only one reason to change, meaning it should have only one job or responsibility.
- **O**: Open/Closed Principle (OCP) - Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means that you should be able to add new functionality without changing existing code.
- **L**: Liskov Substitution Principle (LSP) - Objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program.
- **I**: Interface Segregation Principle (ISP) - Clients should not be forced to depend on interfaces they do not use. This means that you should create specific interfaces for different clients rather than a single, general-purpose interface.
- **D**: Dependency Inversion Principle (DIP) - High-level modules should not depend on low-level modules. Both should depend on abstractions. This means that you should depend on abstractions (interfaces) rather than concrete implementations.

# Docstring
- A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the `__doc__` special attribute of that object. The docstring should describe the purpose of the function, class, or module, and provide information about its parameters, return values, and any exceptions that it may raise. Example of a function with a docstring:
```python
def add_numbers(a, b):
    """
    Adds two numbers together.
    """
    return a + b
```
- change with `__doc__` attribute of the function:
```python
def add_numbers(a, b):
    return a + b
add_numbers.__doc__ = """
    Adds two numbers together.
    """
print(add_numbers.__doc__)
```
