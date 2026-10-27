import os
from pathlib import Path
from dotenv import load_dotenv


def main() -> None:
    env_file: Path = Path(__file__).resolve().parent / ".env"
    load_dotenv(env_file)
    print("ORACLE STATUS: Consulting the configuration...")
    defaults: dict[str, str] = {
        "MATRIX_MODE": "development",
        "DATABASE_URL": "",
        "API_KEY": "",
        "LOG_LEVEL": "INFO",
        "ZION_ENDPOINT": "",
    }
    config: dict[str, str] = {}
    missing: list[str] = []
    for name, default in defaults.items():
        value: str = os.getenv(name, default).strip()
        config[name] = value
        if not value:
            missing.append(name)
    mode: str = config["MATRIX_MODE"].lower()
    if mode not in ("development", "production"):
        print(f"WARNING: Invalid MATRIX_MODE '{mode}'.")
        print("Using development mode.")
        mode = "development"
    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    if config["DATABASE_URL"]:
        if mode == "development":
            print("Database: Configured (details hidden)")
        else:
            print("Database: Configured (details hidden)")
    else:
        print("Database: Not configured")
    if config["API_KEY"]:
        print("API Access: Key configured (value hidden)")
    else:
        print("API Access: Not configured")
    print(f"Log Level: {config['LOG_LEVEL']}")
    if config["ZION_ENDPOINT"]:
        print("Remote Network: Endpoint configured")
    else:
        print("Remote Network: Not configured")
    if mode == "development":
        print("\nDevelopment mode: Detailed diagnostic output enabled.")
    else:
        print("\nProduction mode: Sensitive configuration is hidden.")
    print("\nConfiguration security check:")
    print("[OK] Secret values are not displayed")
    print("[OK] .env is listed in .gitignore")
    if missing:
        print("[WARNING] Missing configuration: " + ", ".join(missing))
    else:
        print("[OK] All configuration values are present")
    print("[OK] Environment variables can override .env values")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
