def new_section(msg: str) -> None:
    full_len = 90
    left_part = 10
    if len(msg) >= full_len - left_part:
        raise Exception(f"new_section(msg): len(msg) must be lower than {full_len - left_part}")
    print(f"\n{'-' * left_part}{msg}{'-' * (full_len - len(msg) - left_part)}")