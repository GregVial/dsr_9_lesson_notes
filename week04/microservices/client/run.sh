docker build -t ronlog .
docker run --name rl --link rg:rongen -p 5002:5002 -t ronlog
