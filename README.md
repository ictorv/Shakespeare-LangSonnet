![MIT License](https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge)

# <center> Shakespeare LangSonnet </center>

<p align="center"> 

![screenshot](assets/LangVid.gif)
</p> 

<p align="center">
  <a href="notebook/Model Training.ipynb">Notebook</a> •
  <a href="models/tokenizer.pickle">Tokenizer</a> •
  <a href="models/model_sp.h5">Model</a> 
</p>  


<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#built-with">Requirements</a>
    </li>
    <li><a href="#model-overview">Model Overview</a></li>
    <li><a href="#project-setup">Project Setup</a> </li>
  </ol>
</details>

## About The Project
ShakeLang is **LSTM** based language model trained on **William Shakespeare's Sonnet**. This project require some initial input for proceeding to create poem like Shakespeare.<br>
Create Sonnet's like Shakespeare

## Built With
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white) 
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

## Model Overview
+ Deep Learning Model: LSTM  (350 Node)
+ Optimizer: Adam  
+ Loss: Categorical Crossentropy 
+ Metrice: Accuracy  
+ Trainable params: 2535151 (9.67 MB)
+ Training Epochs: 50


## Project Setup

+ Create and activate the virtual environment
```bash
python -m venv env
```

```bash
source env/Scripts/Activate
```

+ Install Dependencies
```bash
pip install -r requirements.txt
```
+ Running Server
```bash
python manange.py runserver
```
+ Open in Browser
```bash
http://127.0.0.1:8000/
```