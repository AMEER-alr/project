import argparse
import sys
import os

try:
    import importlib.util

    json_csv_path = os.path.join(os.path.dirname(__file__), '..', 'lab05', 'json_csv.py')
    spec = importlib.util.spec_from_file_location("json_csv", json_csv_path)
    json_csv = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(json_csv)

    csv_xlsx_path = os.path.join(os.path.dirname(__file__), '..', 'lab05', 'csv_xlsx.py')
    spec = importlib.util.spec_from_file_location("csv_xlsx", csv_xlsx_path)
    csv_xlsx = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(csv_xlsx)

    json_to_csv = json_csv.json_to_csv
    csv_to_json = json_csv.csv_to_json
    csv_to_xlsx = csv_xlsx.csv_to_xlsx
    
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)

def json2csv_command(args):
    try:
        json_to_csv(args.input, args.output)
        print(f"Successfully converted {args.input} to {args.output}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def csv2json_command(args):
    try:
        csv_to_json(args.input, args.output)
        print(f"Successfully converted {args.input} to {args.output}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def csv2xlsx_command(args):
    try:
        csv_to_xlsx(args.input, args.output)
        print(f"Successfully converted {args.input} to {args.output}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Data Conversion Tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p1 = subparsers.add_parser("json2csv", help="Convert JSON to CSV")
    p1.add_argument("--in", dest="input", required=True, help="Input JSON file")
    p1.add_argument("--out", dest="output", required=True, help="Output CSV file")
    p1.set_defaults(func=json2csv_command)

    p2 = subparsers.add_parser("csv2json", help="Convert CSV to JSON")
    p2.add_argument("--in", dest="input", required=True, help="Input CSV file")
    p2.add_argument("--out", dest="output", required=True, help="Output JSON file")
    p2.set_defaults(func=csv2json_command)

    p3 = subparsers.add_parser("csv2xlsx", help="Convert CSV to XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Input CSV file")
    p3.add_argument("--out", dest="output", required=True, help="Output XLSX file")
    p3.set_defaults(func=csv2xlsx_command)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()