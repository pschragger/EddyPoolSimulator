docker build -i pysim-env .
docker stop pysim_container 
docker remove pysim_container
docker run -d -p 2222:22 --name pysim_container pysim-env
