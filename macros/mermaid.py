
def mermaid(doc, name, content, width=1024):

    # need to do something to make it faster
    md5 = j.data.hash.md5_string(content)
    md5 = bytes(md5.encode())
    md5b = j.core.db.get("docgenerator:mermaid:%s" % name)

    if md5b != md5:
        path = j.sal.fs.getTmpFilePath()
        content2 = ""
        for item in content.split("\n"):
            itemstrip = item.strip()
            if itemstrip != "" and itemstrip[0] == "%":
                continue
            content2 += "%s\n" % item
        j.sal.fs.writeFile(filename=path, contents=content2)
        dest = j.sal.fs.joinPaths(j.sal.fs.getDirName(j.sal.fs.getDirName(doc.path)), "%s.png" % name)
        csspath = "/opt/code/github/jumpscale/docgenerator/macros/cs.css"
        cmd = "cd /tmp;mermaid -p '%s' -w %s -t %s" % (path, width, csspath)
        res = j.do.execute(cmd)
        path2 = path + ".png"
        j.sal.fs.moveFile(path2, dest)
        j.sal.fs.remove(path2)
        j.sal.fs.remove(path)
        doc.docSite.addFile(dest)

        j.core.db.set("docgenerator:mermaid:%s" % name, md5)

    return "![%s.png](%s.png)" % (name, name)
