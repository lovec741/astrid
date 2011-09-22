﻿import cherrypy
import Server
import sys

from cherrypy.process.plugins import Daemonizer
from cherrypy.process.plugins import PIDFile

print sys.argv
if len(sys.argv) < 2:
    print "Specify pid file."
    sys.exit(1)
    
# before mounting anything
Daemonizer(cherrypy.engine).subscribe()
PIDFile(cherrypy.engine, pidfile=sys.argv[1]).subscribe()

cherrypy.tree.mount(Server.root, "/", config=Server.conffile)
cherrypy.engine.start()
cherrypy.engine.block()
