# ARTH - Task 26 👨🏻‍💻 

# Task Description 📄

📌 GUI container on the Docker

🔅 Launch a container on docker in GUI mode 

🔅 Run any GUI software on the container

## Commands to run:-
### To create image

```$ docker build -t <image_name>:<tag> .```
  
### To launch container
```$ docker run -it  -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=:0 <image_name>:<tag>```

Link to linkedin post:- https://www.linkedin.com/posts/samriddhi-mishra_vimaldaga-righteducation-educationredefine-activity-6804678041894191104-PBS8
