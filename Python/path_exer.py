from pathlib import Path

aicore_path = Path('Python')

# list_of_aicore_paths = [i for i in aicore_path.iterdir()]
# print(list_of_aicore_paths)
# print(aicore_path.exists())

# list_of_aicore_dir = [i for i in aicore_path.iterdir() if i.is_dir()]
# print(list_of_aicore_dir)

py_files = [i for i in aicore_path.rglob('*.py')]
print(py_files)
