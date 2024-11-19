# Introduction

## Background

Recently we went through the process of selling our house in the Netherlands and the first quote we had was an automated one from the [funda](https://funda.nl) app. The quote was based on various house characteristics that were already filled in when setting up your house in the app, but also on the current condition of the house which was based on user input. 

I found this very interesting and I decided to build a proxy for that service. Being surrounded by engineers in my family and having studied civil engineering myself, I knew what factors would be the most influential which would allow me to focus on the technical implementation. 

## Objective

The goals for this project are to:

1. build a simple, yet complete, end-to-end pipeline for predicting house prices (see [Part I](methodology.md#part-i-end-to-end-ml-pipeline)),
2. build a web app UI where users can input various characteristics and receive a quick quote (via an api call) (see [Part II](methodology.md#part-ii-streamlit-ui-and-serving-with-fastapi)), and
3. deploy the web app using Docker (see [Part III](methodology.md#part-iii-deployment-with-docker-containers)).

## Tools
![pandas Badge](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=fff&style=plastic)
![scikit-learn Badge](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=fff&style=plastic)
![Streamlit Badge](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=fff&style=plastic)
![FastAPI Badge](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=fff&style=plastic)
![Docker Badge](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff&style=plastic)
![Amazon Web Services Badge](https://img.shields.io/badge/Amazon%20Web%20Services-232F3E?logo=amazonwebservices&logoColor=fff&style=plastic)
![Pytest Badge](https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=fff&style=plastic)
![Material for MkDocs Badge](https://img.shields.io/badge/Material%20for%20MkDocs-526CFE?logo=materialformkdocs&logoColor=fff&style=plastic)

## Commands

The Makefile contains the central entry points for common tasks related to this project.

