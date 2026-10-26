import importlib


def check_dependency(name: str, description: str) -> bool:
    try:
        module = importlib.import_module(name)
        version: str = str(getattr(module, "__version__", "unknown"))
        print(f"[OK] {name} ({version}) - {description}")
        return True
    except ImportError:
        print(f"[MISSING] {name} - {description}")
        return False


def main() -> None:
    print("\nREAGENT STATUS: Loading reagent...\n")
    print("Checking dependencies")

    dependencies: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerica computation ready",
    }

    all_present: bool = True

    for name, description in dependencies.items():
        if not check_dependency(name, description):
            all_present = False

    if not all_present:
        print("\nMissing dependencies. Install them using pip:")
        print("pip install -r ex0/requirements.txt")
        print("Or using Poetry from the project root:")
        print("poetry -C ex0 install")

    print("\npip vs Poetry:")
    print("requirements.txt declares what to install; pip resolves it")
    print("at install time.")
    print("pyproject.toml declares the same constraints, and Poetry")
    print("pins the resolved versions in poetry.lock so every install")
    print("is reproducible.")

    if all_present:
        print("All reagents present and accounted for.")
    else:
        print("Some reagents are missing.")

if __name__ == "__main__":
    main()