from JumpScale import j


def generate(docsite):

    for item in ["public", "static/css", "static/js", "static/img", "themes"]:
        j.sal.fs.symlink("%s/%s" % (docsite.templatePath, item), "%s/template/%s" % (docsite.outpath, item))

    ws = j.tools.docgenerator.webserver + "/%s/out/" % docsite.name

    cmd = "cd %s/template;hugo -b '%s' --config '../src/generate/config.toml' -c '../src' -d '../out' --noChmod --noTimes --canonifyURLs -v" % (
        docsite.outpath, ws)

    print(cmd)
    j.do.execute(cmd)
