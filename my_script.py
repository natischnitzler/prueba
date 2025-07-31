from datetime import datetime

def main():
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Script ejecutado correctamente a las {ahora}")

if __name__ == "__main__":
    main()
