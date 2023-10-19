from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("{}".format(tag))
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_startendtag(self, tag, attrs):
        print("{}".format(tag))
        for name, value in attrs:
            print(f"-> {name} > {value}")


if __name__ == '__main__':
    html_text = '\n'.join(input() for _ in range(int(input())))
    CustomHTMLParser().feed(html_text)
