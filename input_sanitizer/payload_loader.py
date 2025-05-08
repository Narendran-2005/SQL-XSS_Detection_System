def load_payloads(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[!] Payload file not found: {file_path}")
        return []
