import os
import site
import sys


def main() -> None:
    in_venv: bool = sys.prefix != sys.base_prefix

    print("\nLABORATORY STATUS: ", end="")
    if in_venv:
        print("The laboratory is sealed\n")
    else:
        print("You are working in the open\n")

    print(f"Current Python: {sys.executable}")

    if in_venv:
        env_name: str = os.path.basename(sys.prefix)
        print(f"Virtual Enviroment: {env_name}\n")
        print(f"Enviroment Path: {sys.prefix}")
        print("SUCCESS: You are working in an isolated enviroment!")
        print("Safe to install reagetn without affecting")
        print("the global system.")
        print("Reagent installation path:")
        for path in site.getsitepackages():
            print(path)
    else:
        print("Virtual Enviroment: None detected\n")
        print("WARNING: You are in the global enviroment!")
        print("Every reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run:")
        print("python3 -m venv lan_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\acrivate # On Windows\n")
        print("Then run this program again.")
        print("Global paclage installation path:")
        for path in site.getsitepackages():
            print(path)


if __name__ == "__main__":
    main()
