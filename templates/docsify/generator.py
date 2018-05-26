from js9 import j
import pytoml


def generate(docsite):

    docsite.files_copy()

    # # for item in ["static/css", "static/js", "static/img", "themes"]:
    # for item in ["static/css", "static/js", "static/img", "themes"]:
    #     j.sal.fs.symlink("%s/%s" % (docsite.templatePath, item), "%s/%s" % (docsite.outpath, item))

    # T = pytoml.dumps(docsite.config, True)
    # j.sal.fs.writeFile(filename=j.sal.fs.joinPaths(docsite.outpath, "config.toml"), contents=T, append=False)

    # ws = j.tools.docgenerator.webserver + "/%s/public/" % docsite.name

    # cmd = "cd %s/template;hugo -b '%s' --config '../src/generate/config.toml' -c '../src' -d '../out' --noChmod --noTimes --canonifyURLs -v" % (
    #     docsite.outpath, ws)

    # cmd = "cd %s;hugo -b '%s' --noChmod --noTimes  -v --canonifyURLs" % (
    #     docsite.outpath, ws)

    # cmd = "source $HOME/.bash_profile;cd %s;hugo --noChmod --noTimes  -v " % (docsite.outpath)

    # print(cmd)
    # j.sal.process.execute(cmd)

#
