Getting started
===============

## Clone repo

Clone the repository into your favorite folder:
``` bash
git clone https://github.com/nikolaos-mavromatis/house-price-quoting-app.git
```

and navigate to it:
``` bash
cd house-price-quoting-app
```

<!-- ## Python Environment

``` bash
python3 -m venv .venv

source 
``` -->

## Docker Containers

In this project two containers need to be created:

* one for the API, and
* one for the UI.

Since the UI makes a call to the API to receive the prediction based on the user's inputs, the two containers need to communicate with each other.

This is not straightforward, because as per Docker's [documentation page](https://docs.docker.com/engine/network/), containers are by default agnostic to the type of network they are attached to. 

### Setup

Make sure you have docker installed. The easiest way is by [installing Docker Desktop](https://docs.docker.com/desktop/setup/install/mac-install/). A Docker Desktop installation will also install Docker Compose, which is used to spin up the containers.

I used `docker-compose` to build both containers and the network over which they will communicate from a single file. 

``` bash
docker-compose up -d
```

!!! note
    The last part in `docker-compose.yml`, 

    ``` yaml
    networks:
      housing-app:
        driver: bridge
    ```

    takes care of creating the network where the two containers will be able to communicate with each other.


``` bash
[+] Running 3/3
 ✔ Network ames_house_price_prediction_housing-app     Created             0.0s 
 ✔ Container ames_house_price_prediction-app-1         Started             0.2s 
 ✔ Container ames_house_price_prediction-api-1         Started             0.2s
```

### Teardown

Once you are done experimenting, you can remove all containers and networks by running this command:

``` bash
docker-compose down
```

In this case, it should result to the following:
``` bash
[+] Running 3/3
 ✔ Container ames_house_price_prediction-app-1         Removed             0.2s 
 ✔ Container ames_house_price_prediction-api-1         Removed             0.5s
 ✔ Network ames_house_price_prediction_housing-app     Removed             0.1s
```
