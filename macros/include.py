
def include(doc, name, **args):
    name = name.lower()

    doc = j.tools.docgenerator.getDoc(name, die=False)
    if doc != None:
        doc.process()

        newcontent = doc.content

    # if name in self._contentPaths:
    #     newcontent0 = j.sal.fs.fileGetContents(self._contentPaths[name])
    #
    #     newcontent = ""
    #
    #     pre = "#" * self.last_level
    #
    #     for line in newcontent0.split("\n"):
    #         if line.find("#") != -1:
    #             line = pre + line
    #         newcontent += "%s\n" % line

    else:
        newcontent = "ERROR: COULD NOT INCLUDE:%s (not found)" % name
    return newcontent
