from flask import Flask
from redid import Redis, RedisError

# connect to redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

@app.route("/")
def vote():
  html = "<h3>hallo {name}</h3>" \
         "<b>Hostname:</b> {hostname}</br>"

  return = html.fomat(name=os.getenv("NAME), hostname=socket.gethostname())

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
