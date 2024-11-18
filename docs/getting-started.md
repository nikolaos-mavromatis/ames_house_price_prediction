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
 ✔ Network house-price-quoting-app_housing-app     Created                 0.0s 
 ✔ Container house-price-quoting-app-app-1         Started                 0.2s 
 ✔ Container house-price-quoting-app-api-1         Started                 0.2s
```

### Teardown

Once you are done experimenting, you can remove all containers and networks by running this command:

``` bash
docker-compose down
```

In this case, it should result to the following:
``` bash
[+] Running 3/3
 ✔ Container house-price-quoting-app-app-1         Removed                 0.2s 
 ✔ Container house-price-quoting-app-api-1         Removed                 0.5s
 ✔ Network house-price-quoting-app_housing-app     Removed                 0.1s
```
## Use the app

Visit [http://localhost:8501](http://localhost:8501) and experiment with the UI.

This is how it looks like:

![User Interface](assets/UI_Screenshot.png){ width="80%"}
/// caption
The UI was made with Streamlit.
///
    
## Recap
After navigating to the project directory where the project will live, this is the full script to set it up from scratch.

``` bash
git clone https://github.com/nikolaos-mavromatis/house-price-quoting-app.git
cd house-price-quoting-app
docker-compose up -d
open http://localhost:8501/
```

!!! warning
    Don't forget to tear down everything after you have finished.

    ``` bash
    docker-compose down
    ```
