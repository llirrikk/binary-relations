def new_section(msg: str, need_first_nl: bool = True) -> None:
    full_len = 90
    left_part = 10
    if len(msg) >= full_len - left_part:
        raise Exception(f"new_section(msg): len(msg) must be lower than {full_len - left_part}")
    print(need_first_nl * '\n' + f"{'-' * left_part}{msg}{'-' * (full_len - len(msg) - left_part)}")
