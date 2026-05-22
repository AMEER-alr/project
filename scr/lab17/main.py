import sys
from app import MedicalApp
from cli import ConsoleCLI

def main() -> int:
    app = MedicalApp()
    cli = ConsoleCLI(app)
    return cli.run()

if __name__ == "__main__":
    sys.exit(main())