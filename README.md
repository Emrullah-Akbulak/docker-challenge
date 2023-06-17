# Docker Challenge

## How to start

This project uses Docker version 24.0.2 as its only requirement and offers 2 different environments for development and production.

Note: Switching between different workflows requires rebuilding.

### Production

Production workflow can be run with:

```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
```

This workflow uses `Nginx` and `Gunicorn` to serve `React` and `Django` both under http://localhost and applies all needed production optimizations.

The client aka `React App` can be directly accessed from http://localhost and api endpoints are served under http://localhost/api/ address

### Development

Development workflow can be run with:

```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

This workflow does not use any reverse proxy or WSGI and serves `Django` and `React` servers under ports `8000` and `3000` respectively. However, this workflow offers quick refresh for developers to being able to mirror their changes to docker containers while coding to improve ease of development.

Django server is served under http://localhost:8000  
React server is served under http://localhost:3000

## Containers

---

### <u>Django</u>

This container holds the RestAPI Logic of the whole app using Django version 4.2.2 and Gunicorn. The container either uses the basic Django server for development or Gunicorn based on current workflow.

#### <b>Endpoints</b>

> `Path:` **/**  
> `Paremeters:` None  
> `Explanation:` This endpoint returns string "Hello World!" to show that the server is working. (Only in development)

> `Path:` **/api/heat**  
> `Paremeters:`
>
> ```py
> limit: int or None
> ```
>
> `Explanation:` This endpoint either returns all the heat datas or the last x amount of heat data based on passed parameter `limit`.

### <u>Web</u>

This container both holds the ReactJS for Client and Nginx for static file serving and reverse proxy server. The container either uses the basic React server for development or Nginx to serve both RestAPI and client files based on current workflow.

#### <b>Pages</b>

> `Name:` Home  
> `Path:` **/**  
> `Explanation:` This is the main and the only path for the client-side. It only serves the graph for last 30 heat data. The graph updates every 5 seconds.

### <u>Sensor</u>

This container holds a simple script that write 3 random heat data to PostgresDB every 5 seconds.

### <u>Postgres</u>

This container holds a PostgresDB for other containers.
