# Deep Learning Notes & Projects

## Sigilizer
Trains GAN on symbols obtained from symboldictionary.net to generate novel sigils. Over 2k symbols were downloaded from the website, and ~1.7k were used for training. I manually removed some that didn't fit my personal subjective sigil criteria. The sigils were converted to grayscale. Not doing so amplifies the importance of residual color found in some of the images, resulting in test images like:  

![test_arange_83](https://user-images.githubusercontent.com/4405597/34166933-467493a8-e4ae-11e7-9306-ae0137b79f4b.png)  

The DCGAN code should take an input uniform distribution between -1 and 1 to generate test images, but it was initially using an input zero matrix. I had to change this but I think the issue should be fixed in [this commit](https://github.com/carpedm20/DCGAN-tensorflow/pull/233/commits/88e6d80cc06f5851b9b99fadc78d2a2651215ff6). Not doing so results in something vaguely resembling primitive rorschach blots:   

![test_arange_83_480](https://user-images.githubusercontent.com/4405597/34166932-465e6e0c-e4ae-11e7-84ef-3b49e64f6aac.png)

The DCGAN code is carpedm20's and can be found [here](https://github.com/carpedm20/DCGAN-tensorflow).  

Here are some of the results after training for 1 day on a CPU:  

![train_92_0006](https://user-images.githubusercontent.com/4405597/34166934-468425b6-e4ae-11e7-9078-1c5bf43737ec.png)

Results after 2 days of training (results seemed to visually converge after 1.5 days of training, though discriminator and generator losses continued to fluctuate):  

![final_test1](https://user-images.githubusercontent.com/4405597/34166929-46334f1a-e4ae-11e7-82b4-ea6e3b61f54a.png)
![final_test2](https://user-images.githubusercontent.com/4405597/34166930-46400aac-e4ae-11e7-8ef8-3da31b8bfe66.png)
![final_test3](https://user-images.githubusercontent.com/4405597/34166931-46543c8e-e4ae-11e7-9a55-d5e076c66c03.png) 

Overall it seems to be developing towards a proto-Celtic-Satanic aesthetic.  

## Using FloydHub


