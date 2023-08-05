<h1 align="center"> 📄✏ Wafer Fault Detection Project <h1>

# Brief Overview
In electronics, a **wafer** (also called a slice or substrate) is a thin slice of semiconductor, such as a crystalline silicon (c-Si), used for the fabrication of integrated circuits and, in photovoltaics, to manufacture solar cells. The wafer serves as the substrate(serves as foundation for contruction of other components) for microelectronic devices built in and upon the wafer. 

It undergoes many microfabrication processes, such as doping, ion implantation, etching, thin-film deposition of various materials, and photolithographic patterning. Finally, the individual microcircuits are separated by wafer dicing and packaged as an integrated circuit.

<h2 align="center">⛩ Architecture

 
 
![image](https://user-images.githubusercontent.com/85347886/137638160-1e2932af-e0ee-4dec-a00f-8552b06a96d0.png)
<h2>

##	Functional Architecture
<h2 align = "center">

![image](https://user-images.githubusercontent.com/85347886/137639174-37f387fb-6597-473b-877c-9261ff9522b6.png)

</h2>

 



💿 Installing
1. Environment setup.
```
conda create --prefix venv python==3.8 -y
```
## Why Do We Need ENV.
OS is a universal environment, one must not create project dependency in the universal environment as this idea may lead to overlap with other projects. We need to create isolated environment such no two projects share same resources. Such isolations are important because different projects will need different dependencies. Conda will help us in preserving os resources as an environment solely for the use of project in which that environment is active.

Anaconda on the other hand provides us with all necessary dependencies pre-installed in our environment helping in our data science projects.

```
conda activate venv/
````
2. Install Requirements and setup
```
pip install -r requirements.txt

```
## Need of setup.py File.
In any project our main logic (Code) folder can be seen as a package, which needs to be dumped in our local environment. For example, in this project src folder consists of all the logic, it can be seen as a package and to make my environment identify it as a package I need to create a setup.py file.

To execute the setup.py file use below command

```

python setup.py install
```
After executing the above command on executing pip list, we could see our src folder as a package.

5. Run Application
```
python app.py
```

🔧 Built with
- flask (For Api Creation)
- Python 3.8 (Core Language)
- Machine learning 
- Scikit learn (ML Library)
- SQL (For Database)
- numpy
- Pandas
- 🏦 Industrial Use Cases