import terminatorlib.plugin as plugin
from subprocess import call
 
AVAILABLE = ['OtpAuthPluginHandler']
 
class OtpAuthPluginHandler(plugin.URLHandler):
  capabilities = ['url_handler']
  handler_name = 'otpauth_plugin_handler'
  match = '\\botpauth:.*\\b'
 
  def callback(self, url):
    ggl_url = 'https://chart.googleapis.com/chart?chs=200x200&cht=qr&chl=200x200&chld=M|0&cht=qr&chl=' + url
    return(ggl_url)
