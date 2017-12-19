# Deep Learning Notes & Projects

## Sigilizer
Trains GAN on symbols obtained from symboldictionary.net to generate novel sigils. Over 2k symbols were downloaded from the website, and ~1.7k were used for training. I manually removed some that didn't fit my personal subjective sigil criteria. The sigils were converted to grayscale. Not doing so amplifies the importance of residual color found in some of the images, resulting in test images like:  

![test_arange_83](https://user-images.githubusercontent.com/4405597/34166933-467493a8-e4ae-11e7-9306-ae0137b79f4b.png)  

The DCGAN code should take an input uniform distribution between -1 and 1 to generate test images, but it was initially using an input zero matrix. I had to change this but I think the issue should be fixed in [this commit](https://github.com/carpedm20/DCGAN-tensorflow/pull/233/commits/88e6d80cc06f5851b9b99fadc78d2a2651215ff6). Not doing so results in something vaguely resembling primitive rorschach blots:   

![test_arange_83_480](https://user-images.githubusercontent.com/4405597/34166932-465e6e0c-e4ae-11e7-84ef-3b49e64f6aac.png)

The DCGAN code is carpedm20's and can be found [here](https://github.com/carpedm20/DCGAN-tensorflow).  

Here are some of the results after training for 1 day on a CPU (looking ultrasound-y):  

![train_92_0006](https://user-images.githubusercontent.com/4405597/34166934-468425b6-e4ae-11e7-9078-1c5bf43737ec.png)

Results after 2 days of training (results seemed to visually converge after 1.5 days of training, though discriminator and generator losses continued to fluctuate):  

![final_test1](https://user-images.githubusercontent.com/4405597/34166929-46334f1a-e4ae-11e7-82b4-ea6e3b61f54a.png)
![final_test2](https://user-images.githubusercontent.com/4405597/34166930-46400aac-e4ae-11e7-8ef8-3da31b8bfe66.png)
![final_test3](https://user-images.githubusercontent.com/4405597/34166931-46543c8e-e4ae-11e7-9a55-d5e076c66c03.png) 

Overall it seems to be developing towards a proto-Celtic-Satanic aesthetic.  

The data prep code can be found in `sigilizer/`. The DCGAN code was slightly modified to run on FloydHub and can be found in the following places: 

* Command to execute training job: https://www.floydhub.com/morganeciot/projects/sigilizer
* Repository where code & data are found: https://www.floydhub.com/morganeciot/datasets/sigilizer 

## Using FloydHub
[FloydHub](https://www.floydhub.com/) is a bit of toy alternative to AWS for running deep learning projects. I'm using it for personal projects but wouldn't recommend it for anything larger (for example, you can't even ssh into the cluster your project is running on). But it circumvents having to setup your own deep learning environment and allows you to compute on their GPU clusters, meaning I can reduce my train time from hours/days to mere minutes.  

### Floyd projects vs. datasets
Floyd separates data from code. Code should be associated with a **project** and data should be associated with a **dataset**. Data doesn't change much, but you might be continuously tweaking your code and you don't want to reupload it each time you make a change. The **mount point** is what connects your code to your data, and you'll specify that when you run a command on Floyd.  

### Floyd input vs. output
When floyd runs your code, it accesses any external data sources from the **mount point**, which is a directory located in in the root of the filesystem. The default mount point is `/input`. When your code tries to write results, floyd expects them to be written to the root `/output` directory. So all of your references to data ingest need to be preceded by `/input` and all your references to any output (such as checkpoints or final results) need to point to `/output`.    

### Floyd setup
First visit FloydHub and register for an account on FloydHub. Go through email verification, obtain api token, etc. Install the floyd client: 

```
# install the floyd client
pip install -U floyd-cli

# login to floyd to authenticate (will open browser)
floyd login
```  

Navigate to your project repository. My directory structure looks like:  

```
- DCGAN-tensorflow-sigilizer/
-- data/
--- sigils/
-- main.py
-- model.py
-- ops.py
-- utils.py
- sigilizer
-- run_sigilizer_on_floyd.sh
```  

I'm using python3 and had to add the following to my `.bashrc`:
```
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```
This avoids the following error (more information [here](http://click.pocoo.org/5/python3/):  
```
Traceback (most recent call last):
  ...
RuntimeError: Click will abort further execution because Python 3 was
  configured to use ASCII as encoding for the environment. Either switch
  to Python 2 or consult http://click.pocoo.org/python3/ for
  mitigation steps.
 ```
 
Initialize the project:  
 
```
cd sigilizer/
floyd init sigilizer
```  

Initialize and upload the dataset:  

```
cd DCGAN-tensorflow-sigilizer/

# dataset will be called "sigilizer"
floyd data init sigilizer

# upload data (version 1)
floy data upload
```  

Run the project:  

```
cd sigilizer/

floyd run --gpu --env tensorflow-0.12 --data morganeciot/datasets/sigilizer/1:input "bash run_sigilizer_on_floyd.sh"
```  

The default env is TF but I'm making sure it's using the (old) version the DCGAN code requires. You can view all supported environments [here](https://docs.floydhub.com/guides/environments/). The `--data` option allows me to specify an uploaded dataset to use with the project. `1` means I'm using version 1 of that dataset. `input` is the root input directory, or the mount point that links the data to the code. In quotes is the command I'm running. The bash script that I'm ultimately running looks like:  

```
python main.py \
  --dataset /input/data/sigils \
  --logs_dir /output/logs \
  --checkpoint_dir /output/checkpoint \
  --sample_dir /output/samples \
  --train \
  --crop
```

### Caveats & notes
* Use a `.floydignore` file in your project to ignore files. Datasets don't yet support this, though, so you can't ignore files in your uploaded datasets.
* Floyd envs come preinstalled with numpy, scipy, and a bunch of useful libraries, but you can [install extra dependencies](https://docs.floydhub.com/guides/jobs/installing_dependencies/) pretty easily
* Don't put data or anything large in your code. FloydHub uploads your code, then downloads and initializes the env each time you run a command, so there's significant overhead to using `run`. 
