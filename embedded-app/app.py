import requests
import yaml

def main():
    print("Embedded app running")
    print(f"Requests version: {requests.__version__}")
    print(f"PyYAML version: {yaml.__version__}")

if __name__ == "__main__":
    main()
