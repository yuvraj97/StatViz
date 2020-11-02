import BeautifulSoup
import os

def init(state):
    # cookies = state.__header["Cookie"]
    js = """Hello world!"""

    # Insert the script in the head tag of the static template inside your virtual environement
    index_path = os.path.join(os.path.dirname(st.__file__), "static", "index.html")
    soup = BeautifulSoup(index_path.read_text(), features="lxml")
    if not soup.find(id='custom-js'):
        script_tag = soup.new_tag("script", id='custom-js')
        script_tag.string = GA_JS
        soup.head.append(script_tag)
        index_path.write_text(str(soup))
        