import re

def main():
    html = input("HTML: ")
    print()
    print(parse(html))

def parse(s):
    match = re.search(r'src="([^"]+)"', s)
    if match:
        src = match.group(1)
        video_id_match = re.search(r'/embed/(\w+[^"])', src)
        if video_id_match:
            video_id = video_id_match.group(1)
            return f'https://youtu.be/{video_id}'
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    main()
