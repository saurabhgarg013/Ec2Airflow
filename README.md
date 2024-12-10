# Ec2Airflow

https://docs.docker.com/engine/install/rhel/
You can install Docker Engine

sudo dnf -y install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo

Install the Docker packages.
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl enable --now docker

verify that the installation is successful by running the hello-world image:
sudo docker run hello-world

#Set Up Airflow Directory
mkdir airflow && cd airflow

#create docker compose file
vi docker-compose.yml

mkdir -p ./dags ./logs ./plugins   ./scripts

sudo chmod -R 777 ./logs ./dags ./plugins ./scripts

sudo mkdir -p /opt/airflow/dags/
sudo mkdir -p /opt/airflow/logs/
sudo mkdir -p /opt/airflow/plugins/
sudo mkdir -p /opt/airflow/scripts/

#run docker compose
sudo docker compose up -d

#check docker container run or not
sudo docker ps

#if contanier not run then you need to check logs
sudo docker logs airflow


#want to stop
sudo docker compose down

docker exec -it airflow /bin/bash

#To ensure that the airflow user inside the Docker container can read and write to these directories
#chown is important to ensure that the airflow user can access and modify files within these directories.
sudo chown -R airflow:airflow /opt/airflow
sudo chown -R airflow:airflow /opt/airflow/logs/
sudo chown -R airflow:airflow /opt/airflow/plugins/
sudo chown -R airflow:airflow /opt/airflow/scripts/


#can check logs
sudo docker logs airflow

#connect with postgres
sudo docker exec -it postgres psql -U airflow -d airflow

#list of table
\dt
SELECT * FROM dag;
SELECT * FROM task_instance;
SELECT * FROM log;

#access airflow 

http://ec2-public-ip:8080  
