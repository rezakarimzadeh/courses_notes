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