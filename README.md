# Deep Learning Notes & Projects

## Sigilizer
Trains GAN on symbols obtained from symboldictionary.net to generate novel sigils. Over 2k symbols were downloaded from the website, and ~1.7k were used for training. I manually removed some that didn't fit my personal subjective sigil criteria. The sigils were converted to grayscale. Not doing so amplifies the importance of residual color found in some of the images, resulting in test images like:  

<test_arange_83.png>  

The DCGAN code should take an input uniform distribution between -1 and 1 to generate test images, but it was initially using an input zero matrix. I had to change this but I think the issue should be fixed in [this commit](https://github.com/carpedm20/DCGAN-tensorflow/pull/233/commits/88e6d80cc06f5851b9b99fadc78d2a2651215ff6). Not doing so results in something vaguely resembling primitive rorschach blots:   

<test_arange_83_480.png>  

The DCGAN code is carpedm20's and can be found [here](https://github.com/carpedm20/DCGAN-tensorflow).  

Here are some of the results after training for 1 day on a CPU:  

<train_92_0006.png>  

I trained for 2 days on my CPU, which was probably unnecessary as results seem to visually converge after 1 day (though the discriminator and generator losses sort of continued to fluctuate):  

<final_test1.png>
<final_test2.png>
<final_test3.png>  

Overall it seems to be developing a proto-Celtic-Satanic taste.  

## Using FloydHub


