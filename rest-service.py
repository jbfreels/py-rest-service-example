#!/usr/bin/env python
import web
import core.services as services

PORT = 8080

class RestService (web.application):
  def run (self, port=8080, *middleware):
    func = self.wsgifunc (*middleware)
    return web.httpserver.runsimple (func, ('0.0.0.0', port))

if __name__ == "__main__": 
  routes = services.Index ()
  app = RestService (routes.urls, globals ())
  app.run (port=PORT)