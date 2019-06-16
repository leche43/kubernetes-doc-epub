import requests_html as rh
import pypandoc
import sys
import os

directories = [\
                   "Setup",
                   "Concepts",
                   "Tasks",
                   "Tutorials",
                   "Reference",
                   "Contribute"
                   ]

def generate_directory_epub(url, name, s=None):
    s = rh.HTMLSession() if not s else s
    r1 = s.get(url)

    html = ""
    anchors = r1.html.find('.item')
    links = [a.absolute_links.pop() for a in anchors]
    # links = filter(lambda href: href.find('/scratch/') == -1, links) # filter out links

    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')

    if not os.path.exists('./epub/'):
        os.makedirs('./epub/')

    print("downloading...")
    for l1 in links:
        r2 = s.get(l1)
        # r2.html.render()
        div = r2.html.find('#docsContent', first=True)
        if div:
            try:
                if name in ["Setup", "Tutorials", "Reference"]:  # will give duplicate id error, go through pages one by one to skip error page
                    print("testing " + l1, end='')
                    pypandoc.convert_text(div.html, "epub3", format="html", outputfile="./tmp/kubernetes_epub_doc_tmp.epub", extra_args=[])
                    print(" works")
            except Exception as e:
                print(" failed!")
                print(e)
            else:
                html += div.html
        with open("./tmp/{}.html".format(name), "wt", encoding="utf-8") as f:
            f.write(html)

    print("generating epub for " + name)
    try:
        pypandoc.convert_text(html, "epub3", format="html", outputfile="./epub/{}.epub".format(name), extra_args=['--css=codeblock_wrap.css', '--epub-metadata=./metadata.xml'])
    except Exception as e:
        print(e)

if __name__ == '__main__':
    s = rh.HTMLSession()
    directories_pairs = [("https://kubernetes.io/docs/{}/".format(n.lower()), n) for n in directories]
    for url, name in directories_pairs:
        print(name)
        generate_directory_epub(url, name)
