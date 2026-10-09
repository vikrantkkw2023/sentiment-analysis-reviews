import importlib

libs = ["pandas", "numpy", "sklearn", "matplotlib", "seaborn", "jupyter_core", "ipykernel"]
for lib in libs:
    try:
        m = importlib.import_module(lib)
        print(f"OK  {lib} {getattr(m, '__version__', '')}")
    except ImportError:
        print(f"MISSING  {lib}")