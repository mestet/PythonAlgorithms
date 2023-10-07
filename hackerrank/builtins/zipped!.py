def yum(text, f):
    return [f(_) for _ in text.split()]


def process():
    n, m = yum(input(), int)
    lines = []
    for it in range(m):
        lines.append(yum(input(), float))
    for chunk in zip(*lines):
        print(f'{sum(chunk) / len(chunk):.1f}')


if __name__ == "__main__":
    process()
